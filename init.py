# -*- coding: utf-8 -*
from MFSharif.models import *
def init():
    cat1, ok = Category.objects.get_or_create(name='زنانه')
    cat2, ok = Category.objects.get_or_create(name='مردانه')

    sub1, ok = Category.objects.get_or_create(name='کفش')
    sub2, ok = Category.objects.get_or_create(name='لباس')
    sub3, ok = Category.objects.get_or_create(name='جواهرات')
    sub4, ok = Category.objects.get_or_create(name='عطر')
    sub5, ok = Category.objects.get_or_create(name='ساعت')
    sub6, ok = Category.objects.get_or_create(name='کیف')
    sub7, ok = Category.objects.get_or_create(name='کفش')
    sub8, ok = Category.objects.get_or_create(name='کت و شلوار')
    sub9, ok = Category.objects.get_or_create(name='متعلقات')
    sub10, ok = Category.objects.get_or_create(name='عطر')
    sub11, ok = Category.objects.get_or_create(name='ساعت')
    sub12, ok = Category.objects.get_or_create(name='کیف')

    rel1, ok = SubCats.objects.get_or_create(category=cat1, subcategory=sub1)
    rel2, ok = SubCats.objects.get_or_create(category=cat1, subcategory=sub2)
    rel3, ok = SubCats.objects.get_or_create(category=cat1, subcategory=sub3)
    rel4, ok = SubCats.objects.get_or_create(category=cat1, subcategory=sub4)
    rel5, ok = SubCats.objects.get_or_create(category=cat1, subcategory=sub5)
    rel6, ok = SubCats.objects.get_or_create(category=cat1, subcategory=sub6)
    rel7, ok = SubCats.objects.get_or_create(category=cat2, subcategory=sub7)
    rel8, ok = SubCats.objects.get_or_create(category=cat2, subcategory=sub8)
    rel9, ok = SubCats.objects.get_or_create(category=cat2, subcategory=sub9)
    rel10, ok = SubCats.objects.get_or_create(category=cat2, subcategory=sub10)
    rel11, ok = SubCats.objects.get_or_create(category=cat2, subcategory=sub11)
    rel12, ok = SubCats.objects.get_or_create(category=cat2, subcategory=sub12)