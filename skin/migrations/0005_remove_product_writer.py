# Generated by Django 3.1.2 on 2020-10-18 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skin', '0004_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='writer',
        ),
    ]