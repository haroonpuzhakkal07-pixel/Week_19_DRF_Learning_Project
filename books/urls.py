from django.urls import path
from .views import BookListCreateAPIView, BookDetailAPIView
urlpatterns = [
    path('books/', BookListCreateAPIView.as_view()),
    path('books/<int:pk>/', BookDetailAPIView.as_view()),
]