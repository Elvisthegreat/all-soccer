# Generated by Django 4.2.11 on 2024-08-14 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('official', '0008_comment_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='official',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
    ]