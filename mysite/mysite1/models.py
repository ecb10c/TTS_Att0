from django.db import models

# Create your models here.
class Excel(models.Model):
    name = models.CharField('姓名', max_length=20)
    gender = models.CharField('性别',choices=(('M','男'),('F','女')),max_length=1)
    telephone = models.CharField('电话',max_length=20)
    mobile = models.CharField('手机',max_length=11)
