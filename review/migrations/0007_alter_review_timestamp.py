# Generated by Django 5.1.2 on 2024-10-26 03:48

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
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 26, 10, 48, 9, 37664)),
        ),
    ]
