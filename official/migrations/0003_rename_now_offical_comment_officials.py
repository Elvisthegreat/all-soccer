# Generated by Django 4.2.11 on 2024-04-28 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('official', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='now_offical',
            new_name='officials',
        ),
    ]
