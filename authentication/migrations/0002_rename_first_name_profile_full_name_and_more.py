# Generated by Django 5.1.2 on 2024-10-23 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='first_name',
            new_name='full_name',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='last_name',
            new_name='username',
        ),
    ]