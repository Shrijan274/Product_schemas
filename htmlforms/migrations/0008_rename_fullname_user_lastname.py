# Generated by Django 5.0.6 on 2024-05-15 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('htmlforms', '0007_rename_lastname_user_fullname_remove_user_firstname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='fullname',
            new_name='lastname',
        ),
    ]
