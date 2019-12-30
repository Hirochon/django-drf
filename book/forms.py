from django import forms
from .models import Book, BookStock

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'price', 'created_at')

class BookStockForm(forms.ModelForm):
    class Meta:
        model = BookStock
        fields = ('book','quantity')