## Create your models here.
## -*- coding: utf-8 -*-
from django.db import models

class Category(models.Model):
   name = models.CharField(max_length = 50)
   img = models.ImageField('image', upload_to='images/profilepics')
   def __str__(self):
       return str(self.pk)

class SubCats(models.Model):
    category = models.ForeignKey(Category,related_name='creator')
    subcategory = models.ForeignKey(Category,related_name='subcategory')
    def __str__(self):
        return str(self.category.pk)
#
class Product(models.Model):
   name = models.CharField("نام کالا", max_length = 255)
   category = models.ForeignKey(Category, verbose_name = "زیر دسته", on_delete = models.PROTECT)
   unit = models.CharField("واحد شمارش", default = "عدد", max_length = 30)
   price = models.PositiveIntegerField("قیمت")
   description = models.CharField('توضیح', max_length = 255)
   image = models.ImageField('عکس', upload_to='images/products')
   popular = models.BooleanField('پرطرفدار',default=False)
   recommended = models.BooleanField('پرطرفدار',default=False)
   def __unicode__(self):
         return str(self.name)
   def __str__(self):
         return str(self.name)

class PopularProducts(models.Model):
    product = models.ForeignKey(Product,verbose_name='کالا')
    image = models.ImageField('عکس تبلیغاتی', upload_to='images/products')
    def __str__(self):
        return str(self.product.name)

class UploadedImage(models.Model):
    image = models.ImageField('عکس', upload_to='images/products')

class Comment(models.Model):
   comment = models.CharField('نظر', max_length = 1000)
   date = models.DateTimeField( 'زمان', auto_now_add = True)
   name = models.CharField('کاربر',max_length=70)
   product = models.ForeignKey(Product,verbose_name = "محصول")
   def __str__(self):
       return str(self.product.name)

class MarketBasket(models.Model):
    # general fields
    # lastModified = models.DateTimeField(auto_now = True, 'آخرین تغییر')
    totalPrice = models.PositiveIntegerField('مبلغ کل',default = 0)
    customer = models.CharField('کاربر', max_length=255)
    # customer = models.OneToOneField(Customer, related_name = 'marketBasket', verbose_name = u'خریدار')

    # relation with products
    productList = models.ManyToManyField(Product, through = 'MarketBasket_Product')

    # variables
    itemsNum = 0  # should update every time an item removed or added or object created

    def __init__(self, *args, **kwargs):
        super(MarketBasket, self).__init__(*args, **kwargs)
        self.itemsNum = self.items.count()
        print(self.itemsNum)

    @staticmethod
    def createForCustomer(customer):
        MarketBasket.objects.get_or_create(customer = customer)

    def add_item(self, product):
        if self.set_item(product, -1):
            self.itemsNum += 1
            return True
        return False

    def set_item(self, product, number):
        (item, created) = self.items.get_or_create(product = product)
        if number != -1:
            item.number = number
        item.save()
        self.calculateTotalPrice()
        return created

    def remove_item(self, product):
        item = self.items.filter(product = product)
        if item.exists():
            self.itemsNum -= 1
            item.delete()
            self.calculateTotalPrice()
            return True
        return False

    def updateItems(self):
        self.itemsNum = self.items.count()
        self.calculateTotalPrice()

    def calculateTotalPrice(self):
        p = 0
        for item in self.items.all():
            p += item.product.price * item.number
        self.totalPrice = p
        self.save()

    def clear(self):
        self.totalPrice = 0
        self.items.all().delete()
        self.save()
        self.itemsNum = 0


class MarketBasket_Product(models.Model):
    # foreign keys
    basket = models.ForeignKey(MarketBasket, related_name = 'items')
    product = models.ForeignKey(Product, related_name = 'baskets')

    # fields
    number = models.IntegerField(default = 1)
