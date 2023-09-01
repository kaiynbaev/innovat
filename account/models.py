
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserModelManager
# from posts.models import Posts
 
class UserModel(AbstractUser):
    username = models.CharField
    email = models.EmailField(db_index=True, unique=True, max_length=200, null=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=50, null=True)
    city_address = models.CharField(max_length=200)
    #posts = models.ForeignKey(Posts, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    objects = UserModelManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number', 'city_address']
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
