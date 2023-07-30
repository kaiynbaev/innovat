
from rest_framework.routers import SimpleRouter
from .views import PostsViewSet



router = SimpleRouter()

router.register(
    prefix=r'api/v1/posts', viewset=PostsViewSet
)




