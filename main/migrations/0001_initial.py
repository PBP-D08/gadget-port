# Generated by Django 5.1.2 on 2024-10-22 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MoodEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mood', models.CharField(max_length=255)),
                ('time', models.DateField(auto_now_add=True)),
                ('feelings', models.TextField()),
                ('mood_intensity', models.IntegerField()),
            ],
        ),
    ]
