from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post, Comment, Like  # Added Like
from accounts.serializers import UserSerializer 

CustomUser = get_user_model()

# My existing UserSerializer (lightweight for nesting)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']
        read_only_fields = ['followers']

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), write_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at', 'comments']

# New: LikeSerializer
class LikeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), write_only=True)

    class Meta:
        model = Like
        fields = ['id', 'user', 'post', 'created_at']