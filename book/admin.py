from django.contrib import admin
from .models import Book, BookStock

admin.site.register(Book)
admin.site.register(BookStock)