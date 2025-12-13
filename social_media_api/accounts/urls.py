from django.urls import path, include
from .views import RegisterView, LoginView, ProfileView
from rest_framework.routers import DefaultRouter
from .views import FollowUserView, UnfollowUserView


router = DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),
]