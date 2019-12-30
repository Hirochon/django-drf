# Generated by Django 2.2.9 on 2019-12-30 10:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20, unique=True, verbose_name='タイトル')),
                ('price', models.IntegerField(null=True, verbose_name='価格')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'book',
            },
        ),
        migrations.CreateModel(
            name='BookStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0, verbose_name='在庫数')),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='book.Book', verbose_name='本')),
            ],
            options={
                'db_table': 'bookstock',
            },
        ),
    ]