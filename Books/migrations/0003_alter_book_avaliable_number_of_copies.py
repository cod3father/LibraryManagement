# Generated by Django 3.2.7 on 2021-09-17 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0002_rename_autor_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='avaliable_number_of_copies',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]