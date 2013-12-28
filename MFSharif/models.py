# # Create your models here.
# -*- coding: utf-8 -*-
from django.db import models
import os
#
# def get_image_path(instance, filename):
#     return os.path.join('img', str(instance.category), filename)
# #
class Category(models.Model):
    name = models.CharField(max_length = 50)
#
# class Mariam(models.Model):
#     maryam = models.ForeignKey(Category)
    # alireza = models.ForeignKey(Category)
class SubCats(models.Model):
    cat = models.ForeignKey(Category)
#     subcategory = models.ForeignKey(Category);
#
class Product(models.Model):
    name = models.CharField("نام کالا", max_length = 255)
    # category = models.ForeignKey(Category, verbose_name = "زیر دسته", on_delete = models.PROTECT)
    # unit = models.CharField("واحد شمارش", default = "عدد", max_length = 30)
    # price = models.PositiveIntegerField("قیمت", help_text = "قیمت را به ریال وارد نمایید")
    # image = models.ImageField('عکس', )
    # image ra bayad ye kari konim :-?

    # description = models.CharField('توضیح')

# class Comment(models.Model):
#     comment = models.CharField('نظر')
#     date = models.DateTimeField( 'زمان', auto_now_add = True)
#     name = models.CharField('user')
#
#
# class MarketBasket(models.Model):
#     # general fields
#     totalPrice = models.IntegerField(default = 0, 'مبلغ کل')
#     customer = models.CharField('خریدار')
#
#     # relation with products
#     productList = models.ManyToManyField(Product, through = 'MarketBasket_Product')
#
#     # variables
#     itemsNum = 0  # should update every time an item removed or added or object created
#
#     def __init__(self, *args, **kwargs):
#         super(MarketBasket, self).__init__(*args, **kwargs)
#         self.itemsNum = self.items.count()
#         print(self.itemsNum)
#
#     @staticmethod
#     def createForCustomer(customer):
#         MarketBasket.objects.get_or_create(customer = customer)
#
#     def add_item(self, product):
#         if self.set_item(product, -1):
#             self.itemsNum += 1
#             return True
#         return False
#
#     def set_item(self, product, number):
#         (item, created) = self.items.get_or_create(product = product)
#         if number != -1:
#             item.number = number
#         item.save()
#         self.calculateTotalPrice()
#         return created
#
#     def remove_item(self, product):
#         item = self.items.filter(product = product)
#         if item.exists():
#             self.itemsNum -= 1
#             item.delete()
#             self.calculateTotalPrice()
#             return True
#         return False
#
#     def updateItems(self):
#         self.itemsNum = self.items.count()
#         self.calculateTotalPrice()
#
#     def calculateTotalPrice(self):
#         p = 0
#         for item in self.items.all():
#             p += item.product.price * item.number
#         self.totalPrice = p
#         self.save()
#
#     def clear(self):
#         self.totalPrice = 0
#         self.items.all().delete()
#         self.save()
#         self.itemsNum = 0
#
#
# class MarketBasket_Product(models.Model):
#     # foreign keys
#     basket = models.ForeignKey(MarketBasket, related_name = 'items')
#     product = models.ForeignKey(Product, related_name = 'baskets')
#
#     # fields
#     number = models.IntegerField(default = 1)
