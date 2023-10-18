from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Item(models.Model):

    def __str__(self):
        return self.item_name
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    item_name=models.CharField(max_length=200)
    item_desc=models.CharField(max_length=200)
    item_price=models.IntegerField()
    item_image=models.CharField(max_length=500,default="https://www.google.com/url?sa=i&url=https%3A%2F%2Falllocal.ca%2Ffood%2Fnorth-nb%2Fgrand-falls%2Fprepared-foods%2Fmaple-cones-2%2Ffeed%2F&psig=AOvVaw1Rwv13oX0M_Ocvp5vwTTD0&ust=1697032174533000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCOjflNPP64EDFQAAAAAdAAAAABAL")

    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})
    