from rest_framework.viewsets import ModelViewSet
from .serializers import (PostsCreateSerializer, PostsGetSerializer , 
                          PostsExchangeGetSerializer, PostsExchangeCreateSerializer)
from .models import Posts, PostExchange
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters as r_filters
from rest_framework.response import Response
# from account.models import UserModel
# from rest_framework.decorators import api_view
# from .forms import PostForm
# from rest_framework import status
# from rest_framework.response import Response

# from rest_framework import filters


class PostsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Posts.objects.all()
    filter_backends = (r_filters.SearchFilter,)
    serializer_class = PostsGetSerializer
    # filterset_fields = ('Account__username',)
    search_fields = ('Posts__title',)
    
    def perform_create(self, serializer):
        serializer.save(UserProfile=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return Posts.objects.filter(author=user)

    def get_serializer_class(self):
        if self.action == 'list':
            return PostsGetSerializer
        elif self.action == 'create':
            return PostsCreateSerializer
        return PostsGetSerializer


    
class PostExchangeViewSet(ModelViewSet):
    
    permission_classes = [IsAuthenticated]
    serializer_class = PostsExchangeGetSerializer
    search_fields = ('PostsExchange__sender',)
    queryset = PostExchange.objects.all()
        
    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
        
        
    def get_queryset(self):
        user = self.request.user
        return PostExchange.objects.filter(sender=user)
    
    
    def get_serializer_class(self):
        if self.action == 'list':
            return PostsExchangeGetSerializer
        elif self.action == 'create':
            return PostsExchangeCreateSerializer
        return PostsExchangeGetSerializer
    
    def update_status(self, request, *args, **kwargs):
        PostsExchange = self.get_object()  
        new_status = request.data.get('new_status')  
        if PostsExchange.update_status(new_status):
            return Response({'message': 'Статус успешно обновлен'})
        else:
            return Response({'message': 'Неверный статус'}, status=400)


    def __str__(self) -> str:
        return f"Exchange {self.id}: {self.sender} -> {self.receiver}"
    
# @api_view(['POST'])
# def create_post(request):
#     if request.method == 'POST':
#         form = PostForm(request.data)
#         if form.is_valid():
#             form.save()
#             return Response({'message': 'Post created'}, status=status.HTTP_201_CREATED)
#         return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    