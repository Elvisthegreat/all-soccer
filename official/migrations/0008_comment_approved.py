# Generated by Django 4.2.11 on 2024-08-14 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('official', '0007_official_updated_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
