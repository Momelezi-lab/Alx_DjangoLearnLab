from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import CustomUser  
from .serializers import UserSerializer 

class FollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()  
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['post']

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser, id=user_id)
        if user_to_follow == request.user:
            return Response({'error': 'Cannot follow yourself'}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.add(user_to_follow)
        serializer = UserSerializer(user_to_follow)
        return Response({
            'message': f'Now following {user_to_follow.username}',
            'user': serializer.data
        }, status=status.HTTP_201_CREATED)

class UnfollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()  
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['post']

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
        if user_to_unfollow not in request.user.following.all():
            return Response({'error': 'Not following this user'}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.remove(user_to_unfollow)
        return Response({'message': f'Unfollowed {user_to_unfollow.username}'}, status=status.HTTP_200_OK)

