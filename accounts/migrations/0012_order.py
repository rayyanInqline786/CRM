# Generated by Django 3.2.7 on 2021-11-26 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_customer_product_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Out for delievery', 'Out for delievery'), ('Delieverd', 'Delievered')], max_length=200, null=True)),
                ('customers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customer')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.product')),
            ],
        ),
    ]
