from django.db import models

# Create your models here.


# blueprint to create database table

class Item(models.Model):
    
    def __str__(self):
        return self.item_name
    
    item_name=models.CharField(max_length=200)
    item_desc=models.CharField(max_length=200)
    item_price=models.IntegerField()
    item_img=models.CharField(max_length=500)