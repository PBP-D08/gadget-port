# Generated by Django 5.1.2 on 2024-10-23 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_rename_first_name_profile_full_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=31),
        ),
    ]
