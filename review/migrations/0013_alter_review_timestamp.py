# Generated by Django 5.1.2 on 2024-10-27 05:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0012_alter_review_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 27, 12, 3, 31, 414834)),
        ),
    ]