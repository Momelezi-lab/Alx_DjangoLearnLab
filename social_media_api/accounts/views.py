from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):  # Or ModelViewSet if you allow full CRUD
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Optional: Only show public profiles or followed users
        return self.queryset

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def follow(self, request, pk=None):
        user_to_follow = get_object_or_404(User, pk=pk)
        if user_to_follow == request.user:
            return Response({'error': 'Cannot follow yourself'}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.add(user_to_follow)
        return Response({'message': f'Now following {user_to_follow.username}'}, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def unfollow(self, request, pk=None):
        user_to_unfollow = get_object_or_404(User, pk=pk)
        if user_to_unfollow not in request.user.following.all():
            return Response({'error': 'Not following this user'}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.remove(user_to_unfollow)
        return Response({'message': f'Unfollowed {user_to_unfollow.username}'}, status=status.HTTP_200_OK)

    # Optional: Check follow status
    @action(detail=True, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def is_following(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        following = request.user.is_following(user)
        return Response({'is_following': following})