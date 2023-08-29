from rest_framework import serializers
from .models import Posts


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts    
        fields = ['title', 'image', 'genre', 'description', 'author' , 'status'] # need to add profile

