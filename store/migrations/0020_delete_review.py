# Generated by Django 4.2.3 on 2023-09-30 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_remove_order_transaction_id_remove_order_zip_code'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
    ]
