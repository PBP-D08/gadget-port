# Generated by Django 5.1.1 on 2024-10-24 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_katalog_image_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='katalog',
            name='image_link',
        ),
    ]