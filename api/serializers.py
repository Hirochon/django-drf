from django.core.validators import RegexValidator
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    """本モデル用シリアライザ"""

    class Meta:
        # 対象のモデルクラスを指定
        model = Book
        # 利用しないモデルのフィールドを指定
        exclude = ['created_at']
        validators = [
            # タイトルと価格にでユニークになっていることを検証
            UniqueTogetherValidator(
                queryset=Book.objects.all(),
                fields=('title','price'),
                message="タイトルと価格でユニークになっていなければいけません。"
            ),
        ]
        extra_kwargs = {
            'title' : {
                'validators' : [
                    RegexValidator(
                        r'^D.+$', message="タイトルは「D」で始めてください。"
                    ),
                ],
            },
        }

    def validate_title(self, value):
        """タイトルに対するバリデーションメソッド"""
        if 'Java' in value:
            raise serializers.ValidationError("タイトルには「Java」を含めないでください。")
        return value

    def validate(self, data):
        """複数のバリデーションメソッド"""
        title = data.get('title')
        price = data.get('price')
        if title and '薄い本' in title and price and price > 3000:
            raise serializers.ValidationError("薄い本は3,000円を超えてはいけません。")
        return data

class BookListSerializer(serializers.ListSerializer):
    """複数の本モデルを扱うためのシリアライザ"""

    # 対象のシリアライザを指定
    child = BookSerializer()