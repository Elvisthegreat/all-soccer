# Generated by Django 4.2.11 on 2024-08-16 03:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('official', '0010_official_like_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='official',
            name='like_count',
        ),
        migrations.AddField(
            model_name='official',
            name='like_count',
            field=models.ManyToManyField(related_name='likepost', to=settings.AUTH_USER_MODEL),
        ),
    ]