# Generated by Django 3.2.7 on 2021-09-15 13:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(height_field=100, upload_to='profile_pics', width_field=100)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=1, max_length=11, null=1, region=None)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=2)),
                ('birthday', models.DateField(blank=1, null=1)),
                ('address', models.CharField(blank=1, max_length=300, null=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
