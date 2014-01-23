from django.contrib import admin

# Register your models here.
from MFSharif.models import *

admin.site.register(MFUser)
admin.site.register(Product)
admin.site.register(PopularProducts)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(SubCats)
admin.site.register(MarketBasket)
admin.site.register(MarketBasket_Product)

