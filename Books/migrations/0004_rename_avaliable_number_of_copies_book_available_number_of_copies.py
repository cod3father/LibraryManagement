# Generated by Django 3.2.7 on 2021-09-17 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0003_alter_book_avaliable_number_of_copies'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='avaliable_number_of_copies',
            new_name='available_number_of_copies',
        ),
    ]