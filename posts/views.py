from rest_framework.viewsets import ModelViewSet
from .serializers import PostsSerializer
from .models import Posts
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters as r_filters
# from rest_framework.decorators import api_view
# from .forms import PostForm
# from rest_framework import status
# from rest_framework.response import Response

# from rest_framework import filters


class PostsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Posts.objects.all()
    filter_backends = (r_filters.SearchFilter,)
    serializer_class = PostsSerializer
    # filterset_fields = ('Account__username',)
    search_fields = ('Posts__title',)
    
    def perform_create(self, serializer):
        serializer.save(UserProfile=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return Posts.objects.filter(author=user)


# @api_view(['POST'])
# def create_post(request):
#     if request.method == 'POST':
#         form = PostForm(request.data)
#         if form.is_valid():
#             form.save()
#             return Response({'message': 'Post created'}, status=status.HTTP_201_CREATED)
#         return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    