# Generated by Django 3.2.7 on 2021-09-29 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_customer_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='banner1.png', null=True, upload_to='profile_pic'),
        ),
    ]
