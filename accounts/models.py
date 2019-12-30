from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """拡張ユーザーモデル"""
    class Meta:
        db_table = 'custom_user'

    email = forms.EmailField(verbose_name='メールアドレス', required=True)