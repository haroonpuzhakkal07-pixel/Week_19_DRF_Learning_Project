from django.urls import path
from .views import book_list, create_book
urlpatterns = [
    path('books/', book_list),
    path('books/create/', create_book),
]