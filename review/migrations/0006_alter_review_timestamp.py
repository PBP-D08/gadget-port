# Generated by Django 4.2.6 on 2024-10-25 13:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0005_alter_review_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 25, 20, 21, 15, 268358)),
        ),
    ]
