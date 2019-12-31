from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    """本モデル用シリアライザ"""

    class Meta:
        # 対象のモデルクラスを指定
        model = Book
        # 利用しないモデルのフィールドを指定
        exclude = ['created_at']

class BookListSerializer(serializers.ListSerializer):
    """複数の本モデルを扱うためのシリアライザ"""

    # 対象のシリアライザを指定
    child = BookSerializer()