# Generated by Django 3.1.2 on 2020-10-21 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='product',
        ),
    ]
