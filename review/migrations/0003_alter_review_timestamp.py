# Generated by Django 4.2.6 on 2024-10-25 13:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_rename_review_review_review_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 25, 20, 11, 50, 746810)),
        ),
    ]