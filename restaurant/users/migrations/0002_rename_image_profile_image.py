# Generated by Django 4.2.6 on 2023-10-14 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Image',
            new_name='image',
        ),
    ]
