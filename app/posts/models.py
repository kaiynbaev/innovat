# need to add status
from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Заголовок'
    )
    
class Posts(models.Model):
    
    class status_choices(models.TextChoices):
        request_1 = "Ожидание подтверждения"
        request_2 = "Запрос принят"
        request_3 = "Детали обмена согласованы"
        request_4 = "Обмен завершен"
        request_5 = "Отклонен"
        request_6 = "Отменен"
        
#__________________________________________

    profile = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Профиль'
    )
    title = models.CharField(
        max_length=50,
        verbose_name='Заголовок'
    )
    image = models.ImageField(
        upload_to="posts/%Y/%m/%d",
        verbose_name='Фото'
    )
    genre = models.CharField(
        max_length=50,
        verbose_name='Жанр'
    )
    description = models.CharField(
        max_length=500,
        verbose_name='Описание'
    )
    status = models.CharField(
        choices=status_choices
    )
    create_date = models.DateTimeField(
        auto_now_add=True
    )
    update_date = models.DateTimeField(
        auto_now=True
    )
    
    
    
    def __str__(self):
        return f"{self.profile}"
    
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        
