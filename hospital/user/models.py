from django.db import models

# Create your models here.

class User(models.Model):
    userID = models.CharField(max_length=30,primary_key=True,verbose_name="用户id")
    username = models.CharField(max_length=30,verbose_name="用户名")
    phone = models.CharField(max_length=30,verbose_name="联系电话")