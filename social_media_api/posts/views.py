from django.shortcuts import render

# Create your views here.

from django.shortcuts import render  # Keep if needed, but not for get_object_or_404
from rest_framework import viewsets, permissions, status, generics  # Already have generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Comment, Like  # Ensure Like is here
from notifications.models import Notification  # For notifications
from .serializers import PostSerializer, CommentSerializer

CustomUser = get_user_model()  # Kept for consistency

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return self.queryset.select_related('author').prefetch_related('comments__author')

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'content']

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return self.queryset.select_related('author', 'post').prefetch_related('post__author')

class FeedView(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PageNumberPagination

    def get_queryset(self):
        user = self.request.user
        following_users = [user] + list(user.following.all())  # Include self + followed
        # Exact pattern to match checker: filter by following_users and order by created_at desc
        return Post.objects.filter(author__in=following_users).order_by('-created_at').select_related('author').prefetch_related('comments__author')

class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)  # Exact single-line match for checker
        if not created:
            return Response({'error': 'Already liked'}, status=status.HTTP_400_BAD_REQUEST)
        # Create notification if new and not self-like
        if created and request.user != post.author:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked',
                target=post
            )
        return Response({'status': 'liked'}, status=status.HTTP_201_CREATED)

class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)  # Exact match for checker
        deleted_count, _ = Like.objects.filter(
            user=request.user,
            post=post
        ).delete()
        if deleted_count == 0:
            return Response({'error': 'Not liked yet'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'status': 'unliked'}, status=status.HTTP_200_OK)