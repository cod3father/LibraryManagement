# Generated by Django 3.2.7 on 2021-09-23 21:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Books', '0007_alter_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_books', to='Books.author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_books', to='Books.category'),
        ),
        migrations.AlterField(
            model_name='book',
            name='user',
            field=models.ManyToManyField(related_name='user_books', through='Books.Borrowing', to=settings.AUTH_USER_MODEL),
        ),
    ]
