# Generated by Django 4.2.6 on 2023-10-10 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_Image',
            field=models.CharField(default='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.everestkitchenpa.com%2Fassets%2Fpages%2FcoldBeverages.html&psig=AOvVaw1Rwv13oX0M_Ocvp5vwTTD0&ust=1697032174533000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCOjflNPP64EDFQAAAAAdAAAAABAE', max_length=500),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_price',
            field=models.IntegerField(),
        ),
    ]