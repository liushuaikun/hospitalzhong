from django.db import models

# Create your models here.
class Druglists(models.Model):
    drugid = models.CharField(primary_key=True, max_length=100, verbose_name='药品ID')
    name = models.CharField(max_length=50, verbose_name='药品名称')
    type = models.CharField(max_length=256, verbose_name='药品种类')
    explain = models.CharField(max_length=256,verbose_name='药品说明')
    birth = models.CharField(max_length=256, verbose_name='药品生产日期')
    scrap = models.CharField(max_length=256, verbose_name='药品过期日期')
    spec = models.CharField(max_length=256, verbose_name='药品规格')
    drugnum = models.IntegerField(default=0, verbose_name='药品数量')
    export = models.IntegerField(default=0, verbose_name='日出库量')
    address = models.CharField(max_length=256, verbose_name='药品位置')
