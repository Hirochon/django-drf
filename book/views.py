from django.shortcuts import render, redirect
from .forms import BookForm, BookStockForm
from django.views import View
from .models import Book, BookStock
from django.db.models import Q

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

class Bookdesu(View):
    def get(self, request, *args, **kwargs):
        params = {
            'title' : '本一覧',
            'books' : Book.objects.all().order_by('-created_at'),
            'bookstocks' : BookStock.objects.all(),
            'book_pricelesses' : Book.objects.filter(Q(price__gte=1500) & Q(price__lt=2000)),
        }
        return render(request, 'book/lib.html', params)