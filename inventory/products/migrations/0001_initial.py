# Generated by Django 3.2.6 on 2021-08-16 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0005_profile_backgroundimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_description', models.TextField(max_length=500)),
                ('product_unit', models.CharField(max_length=50)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=999)),
                ('product_quantity', models.DecimalField(decimal_places=2, max_digits=999)),
                ('product_status', models.BooleanField()),
                ('product_details', models.TextField(max_length=500)),
                ('product_category', models.CharField(max_length=50)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]
