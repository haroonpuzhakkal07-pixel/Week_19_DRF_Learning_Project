from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # Exact Filtering
    filterset_fields = ['author', 'published_year']
    # Search (Partial Match)
    search_fields = ['title', 'author']
    # Ordering
    ordering_fields = ['published_year', 'title']