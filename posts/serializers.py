from rest_framework import serializers
from .models import Posts, PostExchange


class PostsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts    
        fields = ['title', 'image', 'genre', 'description', 'author'] 
        
class PostsGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['UserProfile', 'title', 'image', 'genre', 'description', 'author']
        
        
        
class PostsExchangeGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostExchange
        fields = ['sender', 'receiver', 'post_offered', 'post_requested', 'status']
        
class PostsExchangeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostExchange
        fields = ['receiver', 'post_offered', 'post_requested']
    
    