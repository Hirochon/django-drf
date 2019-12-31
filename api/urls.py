from django.urls import path
from .views import BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('books/', BookListCreateAPIView.as_view()),
    path('books/<pk>/', BookRetrieveUpdateDestroyAPIView.as_view()),
]