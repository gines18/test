from django.db import models

# Create your models here.


# class Menuitems(models.Model):
#     menu = models.CharField(max_length=100)
#     item = models.CharField(max_length=200)
#     price = models.CharField(max_length=200)


# class MenuCategory(models.Model):
#     menu_category_name = models.CharField(max_length=100)


# class Menu(models.Model):
#     menu_item = models.CharField(max_length=200)
#     price = models.IntegerField(null=False)
#     category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT, default=None )


class Logger(models.Model):
      first_name = models.CharField(max_length=100)
      last_name = models.CharField(max_length=100)
      time_log = models.TimeField()

 
     
  

