# Generated by Django 3.2.7 on 2021-09-20 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0003_rename_title_category_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=150, null=True),
        ),
    ]
