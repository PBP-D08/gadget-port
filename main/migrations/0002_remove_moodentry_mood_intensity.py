# Generated by Django 5.1.2 on 2024-10-23 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moodentry',
            name='mood_intensity',
        ),
    ]