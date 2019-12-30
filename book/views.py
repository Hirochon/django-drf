from django.shortcuts import render, redirect
from .forms import BookForm, BookStockForm
from django.views import View
from .models import Book, BookStock

class BookView(View):
    def get(self, request, *args, **kwargs):
        params = {
            'title' : 'Book登録ページ',
            'form' : BookForm(),
        }
        return render(request, 'book/create.html', params)

    def post(self, request, *args, **kwargs):
        book = BookForm(request.POST, Book())
        book.save()
        return redirect(to='/book/create/stock/')

class BookStockView(View):
    def get(self, request, *args, **kwargs):
        params = {
            'title' : 'Stock数登録ページ',
            'form' : BookStockForm(),
        }
        return render(request, 'book/create_stock.html', params)

    def post(self, request, *args, **kwargs):
        book = BookStockForm(request.POST, Book())
        book.save()
        return redirect(to='/admin/')