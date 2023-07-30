from rest_framework import serializers
from .models import Posts


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts    
        fields = ['profile', 'title', 'image', 'genre', 'description', 'status'] # need to add status

