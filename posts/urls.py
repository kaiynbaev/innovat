from django.urls import path, include
# from .views import create_post
from posts.views import PostsViewSet, PostExchangeViewSet
from rest_framework.routers import SimpleRouter


posts_router = SimpleRouter()

posts_router.register(
    prefix=r'api/v1/posts', viewset=PostsViewSet,
)


posts_exchange_router = SimpleRouter()

posts_exchange_router.register(
    prefix=r'api/v1/exchange/posts', viewset=PostExchangeViewSet
)

urlpatterns = [
    path('', include(posts_router.urls)),
    path('', include(posts_exchange_router.urls))
]
