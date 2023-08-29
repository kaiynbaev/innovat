from .views import ActivateUser
from django.urls import path


urlpatterns = [
    path('auth/accounts/activate/<uid>/<token>', ActivateUser.as_view({'get': 'activation'}), name='activation'),
]