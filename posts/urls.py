from django.urls import path, include
# from .views import create_post
from posts.views import PostsViewSet
from rest_framework.routers import SimpleRouter


posts_router = SimpleRouter()
posts_router.register(
    prefix=r'api/v1/posts', viewset=PostsViewSet
)

urlpatterns = [
    path('', include(posts_router.urls))
]
