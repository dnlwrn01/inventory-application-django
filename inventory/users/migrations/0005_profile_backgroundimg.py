# Generated by Django 3.2.6 on 2021-08-14 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_profileimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='backgroundIMG',
            field=models.ImageField(blank=True, upload_to='static/users/images'),
        ),
    ]