# Generated by Django 4.2.6 on 2024-10-25 06:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=255)),
                ('alamat', models.CharField(max_length=255)),
                ('jam_buka', models.TimeField(default='08:00')),
                ('jam_tutup', models.TimeField(default='22:00')),
                ('nomor_telepon', models.CharField(blank=True, max_length=15, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='store_logo/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
