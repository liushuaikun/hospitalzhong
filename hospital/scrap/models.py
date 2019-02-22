from django.db import models

# Create your models here.
class Breakageafter(models.Model):
    afterID = models.CharField(max_length=200, primary_key=True, verbose_name="报废单ID")
    reason = models.CharField(max_length=300,verbose_name="报废原因")
    drugID = models.CharField(max_length=100, verbose_name='药品ID')
    afterbrugname = models.CharField(max_length=100, verbose_name="报废药品名称")
    damagednum = models.IntegerField(default=0, verbose_name="报废量")
    damagetime = models.DateTimeField(auto_now=True, verbose_name="报废时间")