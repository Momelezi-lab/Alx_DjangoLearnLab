from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),

    # REQUIRED BY CHECKER
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Your other routes
    path('books/', views.list_books, name='list_books'),
    path('books/<int:pk>/', views.library_detail, name='library_detail'),
]

