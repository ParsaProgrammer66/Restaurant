# Generated by Django 4.2.6 on 2023-10-12 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_item_item_image_alter_item_item_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='item_Image',
        ),
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://www.google.com/url?sa=i&url=https%3A%2F%2Falllocal.ca%2Ffood%2Fnorth-nb%2Fgrand-falls%2Fprepared-foods%2Fmaple-cones-2%2Ffeed%2F&psig=AOvVaw1Rwv13oX0M_Ocvp5vwTTD0&ust=1697032174533000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCOjflNPP64EDFQAAAAAdAAAAABAL', max_length=500),
        ),
    ]