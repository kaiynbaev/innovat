from django.db import models
from account.models import UserModel



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
    UserProfile = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='UserProfile',
        null=False
    )
    title = models.CharField(
        max_length=50,
        verbose_name='Название книги'
    )
    image = models.ImageField(
        upload_to="posts/%Y/%m/%d",
        verbose_name='Фото',
    )
    genre = models.CharField(
        max_length=50,
        verbose_name='Жанр'
    )
    description = models.CharField(
        max_length=500,
        verbose_name='Описание'
    )
    author = models.CharField(
        max_length=100,
        verbose_name='Автор книги',
        null=True
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
    REQUIRED_FIELDS = ['title', 'genre', 'description', 'author']
    def __str__(self):
        return f"{self.title}"
   
    # @api_view(['POST'])
    # def create_post(request):
    #     if request.method == 'POST':
    #         form = PostForm(request.data)
    #         if form.is_valid():
    #             form.save()
    #             return Response({'message': 'Post created'}, status=status.HTTP_201_CREATED)
    #         return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        

