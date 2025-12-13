from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView 
from .views import LikePostView, UnlikePostView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view({'get': 'list'}), name='feed'),  
    path('posts/<int:pk>/like/', LikePostView.as_view()),
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view()),
]