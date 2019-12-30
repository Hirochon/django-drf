from django.urls import path
from .views import BookView, BookStockView

urlpatterns = [
    path('create/', BookView.as_view(), name='book_create'),
    path('create/stock/', BookStockView.as_view(), name='bookstock_create'),
]