# Generated by Django 4.2.6 on 2024-10-27 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=255)),
                ('alamat', models.CharField(max_length=255)),
                ('nomor_telepon', models.CharField(blank=True, max_length=15, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='store_logo/')),
                ('jam_buka', models.TimeField(default='08:00')),
                ('jam_tutup', models.TimeField(default='22:00')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
