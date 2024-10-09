from django.db import models

# Create your models here.
from django.db import  models
from  django.forms import   ModelForm

class bookinfo(models.Model):
     name = models.CharField(max_length=20,verbose_name="电影名")
     author = models.CharField(max_length=20,verbose_name="电影导演")
     price = models.IntegerField(verbose_name="票价")
     class Meta:
         verbose_name="电影名称"
         verbose_name_plural="电影信息"
class Book(models.Model):
    book_name =models.CharField(max_length=30)
    book_publisher = models.CharField(max_length=20)
    book_author=models.CharField(max_length=20)


class stuinfo(models.Model):
    sName = models.CharField(max_length=20)
    sNo = models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    deptName=models.CharField(max_length=20)