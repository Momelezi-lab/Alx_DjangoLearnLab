views.py)
"""
Authentication & Permissions Setup:
-----------------------------------
- TokenAuthentication enabled globally in settings.py.
- All API endpoints require authentication unless changed per view.
- Users obtain tokens via POST /api-token-auth/ with username & password.
- BookViewSet uses IsAuthenticated by default.
"""


from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # Only authenticated users can access