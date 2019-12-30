from django.db import models
import uuid
from django.utils import timezone

class Book(models.Model):
    """本モデル"""

    class Meta:
        db_table = 'book'
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name='タイトル', unique=True, max_length=20)
    price = models.IntegerField(verbose_name='価格', null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class BookStock(models.Model):
    """本の在庫モデル"""

    class Meta:
        db_table = 'bookstock'

    book = models.OneToOneField(Book, verbose_name='本', on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='在庫数', default=0)

    def __str__(self):
        return self.book.title + ' (' + str(self.quantity) + '冊)' + ' <' + str(self.book.id) + '>'

# class Publisher(models.Model):
#     """出版社モデル"""

#     class Meta:
#         db_table = 'publisher'

#     id = models.UUIDField()