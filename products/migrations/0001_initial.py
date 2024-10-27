# Generated by Django 4.2.6 on 2024-10-27 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Katalog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
                ('price', models.PositiveIntegerField()),
                ('image_link', models.URLField()),
                ('spec', models.CharField(max_length=512)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.store')),
            ],
        ),
    ]
