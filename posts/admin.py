from django.contrib import admin


from .models import Posts

class ModelPosts(admin.ModelAdmin):
    list_display = ('title', )

admin.site.register(Posts,)