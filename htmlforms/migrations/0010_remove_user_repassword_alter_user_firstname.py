# Generated by Django 5.0.6 on 2024-05-15 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('htmlforms', '0009_user_firstname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='rePassword',
        ),
        migrations.AlterField(
            model_name='user',
            name='firstname',
            field=models.CharField(max_length=32),
        ),
    ]
