from django.db import models

# need to add status




class Account(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Заголовок'
    )
    
    
class Posts(models.Model):
    
    # class status_choices(models.TextChoices):
        
    type_of_status = [
        ("Ожидание подтверждения" , "Ожидание подтверждения"),
        ("Запрос принят" , "Запрос принят"),
        ("Детали обмена согласованы" , "Детали обмена согласованы"),
        ("Обмен завершен" , "Обмен завершен"),
        ("Отклонен" , "Отклонен"),
        ("Отменен" , "Отменен"),
    ]
        
    #__________________________________________


    # profile = models.ForeignKey(
    #     Account,
    #     on_delete=models.CASCADE,
    #     related_name='posts',
    #     verbose_name='Профиль'
    # )
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
        max_length=500,
        choices=type_of_status,
        default=1
    )
    create_date = models.DateTimeField(
        auto_now_add=True
    )
    update_date = models.DateTimeField(
        auto_now=True
    )
 
    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        

