# -*- coding: utf-8 -*
from MFSharif.models import Category, SubCats


def init():
    cat1, ok = Category.objects.get_or_create(name='زنانه', img="Capture.JPG")

    cat2, ok = Category.objects.get_or_create(name='مردانه',  img="Capture.JPG")

    sub1, ok = Category.objects.get_or_create(name='کفش', img="Capture.JPG")
    sub2, ok = Category.objects.get_or_create(name='لباس', img="Capture.JPG")
    sub3, ok = Category.objects.get_or_create(name='جواهرات', img="Capture.JPG")
    sub4, ok = Category.objects.get_or_create(name='عطر', img="Capture.JPG")
    sub5, ok = Category.objects.get_or_create(name='ساعت', img="Capture.JPG")
    sub6, ok = Category.objects.get_or_create(name='کیف', img="Capture.JPG")
    sub7, ok = Category.objects.get_or_create(name='کفش', img="Capture.JPG")
    sub8, ok = Category.objects.get_or_create(name='کت و شلوار', img="Capture.JPG")
    sub9, ok = Category.objects.get_or_create(name='متعلقات', img="Capture.JPG")
    sub10, ok = Category.objects.get_or_create(name='عطر', img="Capture.JPG")
    sub11, ok = Category.objects.get_or_create(name='ساعت', img="Capture.JPG")
    sub12, ok = Category.objects.get_or_create(name='کیف', img="Capture.JPG")

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