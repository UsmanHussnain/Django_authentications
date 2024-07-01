# Generated by Django 5.0.4 on 2024-07-01 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_user_cnic'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='verification_token',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
