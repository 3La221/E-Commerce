# Generated by Django 4.2.3 on 2023-09-11 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sold',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
