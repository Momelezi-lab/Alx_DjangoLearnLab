from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # existing ListAPIView
    path('', include(router.urls)),                        # all CRUD endpoints via router
]