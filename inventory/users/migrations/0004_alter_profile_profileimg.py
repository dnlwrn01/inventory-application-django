# Generated by Django 3.2.6 on 2021-08-14 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_websiteurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileIMG',
            field=models.ImageField(blank=True, upload_to='static/users/images'),
        ),
    ]
