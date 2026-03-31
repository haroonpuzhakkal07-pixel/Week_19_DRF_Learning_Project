from django.urls import path
from .views import book_list_create, book_detail
urlpatterns = [
    path('books/', book_list_create),
    path('books/<int:pk>/', book_detail),
]