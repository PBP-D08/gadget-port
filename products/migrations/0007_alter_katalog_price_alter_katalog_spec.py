# Generated by Django 4.2.6 on 2024-10-25 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_merge_20241025_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='katalog',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='katalog',
            name='spec',
            field=models.CharField(max_length=512),
        ),
    ]
