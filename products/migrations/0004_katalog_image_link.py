# Generated by Django 5.1.2 on 2024-10-24 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_katalog_image_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='katalog',
            name='image_link',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]