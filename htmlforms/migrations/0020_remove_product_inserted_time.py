# Generated by Django 5.0.6 on 2024-07-01 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('htmlforms', '0019_alter_product_inserted_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='inserted_time',
        ),
    ]
