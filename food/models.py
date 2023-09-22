from django.db import models

# Create your models here.


# blueprint to create database table

class Item(models.Model):
    
    def __str__(self):
        return self.item_name
    
    item_name=models.CharField(max_length=200)
    item_desc=models.CharField(max_length=200)
    item_price=models.IntegerField()
    item_img=models.CharField(max_length=500,default="https://imgs.search.brave.com/N9JbF0zYUgn4lLcmuNFkGc7UdGzd8jXgH2NrwvYPMW8/rs:fit:860:0:0/g:ce/aHR0cHM6Ly90NC5m/dGNkbi5uZXQvanBn/LzAzLzE1LzE4LzA5/LzM2MF9GXzMxNTE4/MDkzMl9yaGlYRnJK/TjI3elhDQ2RyZ3g4/VjVHV2JMZDl6VEhI/QS5qcGc")
    