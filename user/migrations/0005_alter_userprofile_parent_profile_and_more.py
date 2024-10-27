# Generated by Django 5.1.2 on 2024-10-27 04:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_profile_username'),
        ('user', '0004_alter_userprofile_profile_subprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='parent_profile',
            field=models.ForeignKey(blank=True, help_text='Only buyers can have additional profiles.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_profile', to='user.userprofile'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to='authentication.profile'),
        ),
        migrations.DeleteModel(
            name='SubProfile',
        ),
    ]