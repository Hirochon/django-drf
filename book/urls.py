from django.urls import path
from .views import BookView, BookStockView, Bookdesu

urlpatterns = [
    path('create/', BookView.as_view(), name='book_create'),
    path('create/stock/', BookStockView.as_view(), name='bookstock_create'),
    path('', Bookdesu.as_view(), name='book_lib'),
]