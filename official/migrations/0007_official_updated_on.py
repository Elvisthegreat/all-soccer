# Generated by Django 4.2.11 on 2024-08-14 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('official', '0006_remove_comment_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='official',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
