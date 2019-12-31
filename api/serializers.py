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
                'error_messages':{
                    'blank':"タイトルは必須です。",
                },
                'validators' : [
                    RegexValidator(
                        r'^貧.+$', message="タイトルは「貧」で始めてください。"
                    ),
                ],
            },
            'price':{
                'error_messages':{
                    'invalid':"価格には整数の値を入力してください。"
                }
            }
        }

    def validate_title(self, value):
        """タイトルに対するバリデーションメソッド"""
        if not '齋藤飛鳥' in value:
            raise serializers.ValidationError("必ず「齋藤飛鳥」を含めてください。")
        elif '貧乳' in value:
            raise serializers.ValidationError("握手会が出禁になるので、「貧乳」を含めないでください。")
        return value

    def validate(self, data):
        """複数のバリデーションメソッド"""
        title = data.get('title')
        price = data.get('price')
        if title and '齋藤飛鳥' in title and price and price <= 50000:
            raise serializers.ValidationError("齋藤飛鳥を含めた本はは50,000円以上でなければいけません。")
        return data

class BookListSerializer(serializers.ListSerializer):
    """複数の本モデルを扱うためのシリアライザ"""

    # 対象のシリアライザを指定
    child = BookSerializer()