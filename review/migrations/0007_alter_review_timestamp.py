# Generated by Django 4.2.6 on 2024-10-25 16:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0006_alter_review_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 25, 23, 18, 31, 474002)),
        ),
    ]
