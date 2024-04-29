# Generated by Django 4.2.11 on 2024-04-29 16:57

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('official', '0003_rename_now_offical_comment_officials'),
    ]

    operations = [
        migrations.AddField(
            model_name='official',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
