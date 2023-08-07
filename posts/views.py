from rest_framework.viewsets import ModelViewSet
from .serializers import PostsSerializer
from .models import Posts
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters as r_filters
# from rest_framework import filters


class PostsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Posts.objects.all()
    filter_backends = (r_filters.SearchFilter,)
    serializer_class = PostsSerializer
    # filterset_fields = ('Account__username',)
    search_fields = ('Posts__title',)
    
    
    

    
