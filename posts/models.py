from django.db import models
from account.models import UserModel



class Posts(models.Model):
    
    UserProfile = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='UserProfile',
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
        


class PostExchange(models.Model):
    
    type_of_status = [
        ("Ожидание подтверждения" , "Ожидание подтверждения"),
        ("Запрос принят" , "Запрос принят"),
        ("Детали обмена согласованы" , "Детали обмена согласованы"),
        ("Обмен завершен" , "Обмен завершен"),
        ("Отклонен" , "Отклонен"),
        ("Отменен" , "Отменен"),
    ]
    
    #_______________________________________________________________
    
    
    sender = models.ForeignKey(
        UserModel, 
        on_delete=models.CASCADE, 
        related_name='exchanges_sent',
        verbose_name='Отправитель'
        )
    receiver = models.ForeignKey(
        UserModel, 
        on_delete=models.CASCADE, 
        related_name='exchanges_received',
        verbose_name='Получатель'
        )
    post_offered = models.ForeignKey(
        Posts, 
        on_delete=models.CASCADE,
        verbose_name='Предлагается'
        )
    post_requested = models.ForeignKey(
        Posts, 
        on_delete=models.CASCADE, 
        related_name='exchanges_received',
        verbose_name='Запрашивается'
        )
    status = models.CharField(
        max_length=500,
        choices=type_of_status,
        default=1,
        verbose_name='Cтатус'   
    )
    create_date = models.DateTimeField(
        auto_now_add=True
    )
    update_date = models.DateTimeField(
        auto_now=True
    )
    REQUIRED_FIELDS = ['sender', 'receiver', 'post_offered', 'post_requested']

    class Meta:
        verbose_name = 'Запрос на обмен'
        verbose_name_plural = 'Запросы на обмен'
        
    def update_status(self, new_status):
        if new_status in self.type_of_status.keys():
            self.status = new_status
            self.save()
            return self.status
        else:
            return f'Нет такого типа статуса'    
        
    def __str__(self) -> str:
        return f'{self.sender} -> {self.receiver}'