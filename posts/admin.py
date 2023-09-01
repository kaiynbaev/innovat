from django.contrib import admin
from .models import Posts, PostExchange

class ModelPosts(admin.ModelAdmin):
    list_display = ('id', 'title',)

admin.site.register(Posts, ModelPosts)
admin.site.register(PostExchange)