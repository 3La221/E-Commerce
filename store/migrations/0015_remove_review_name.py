# Generated by Django 4.2.3 on 2023-09-21 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_alter_orderitem_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='name',
        ),
    ]
