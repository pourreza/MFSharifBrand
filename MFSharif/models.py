# Create your models here.
# -*- coding: utf-8 -*-
from django.db import models
import os

def get_image_path(instance, filename):
    return os.path.join('img', str(instance.category), filename)

class Category(models.Model):
    name = models.CharField(max_length = 50)

class SubCats(models.Model):
    category = models.ForeignKey(Category);
    subcategory = models.ForeignKey(Category);

class Product(models.Model):
    name = models.CharField("نام کالا", max_length = 255)
    category = models.ForeignKey(Category, verbose_name = "زیر دسته", on_delete = models.PROTECT)
    unit = models.CharField("واحد شمارش", default = "عدد", max_length = 30)
    price = models.PositiveIntegerField("قیمت", help_text = "قیمت را به ریال وارد نمایید")
    image = models.ImageField('عکس', )
    # image ra bayad ye kari konim :-?

    description = models.CharField('توضیح')

class Comment(models.Model):
    comment = models.CharField('نظر')
    date = models.DateTimeField( 'زمان', auto_now_add = True)
    name = models.CharField('user')


