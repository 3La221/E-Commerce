# Generated by Django 4.2.3 on 2023-09-11 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_product_new_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='new_price',
            field=models.FloatField(blank=True, default='images/product01.png', null=True),
        ),
    ]
