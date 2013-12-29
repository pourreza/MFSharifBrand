# -*- coding: utf-8 -*
from MFSharif.models import *
sub11, ok = Category.objects.get_or_create(name='ساعت', img="images/profilepics/men_wathc.jpg")
pro1, ok = Product.objects.get_or_create(name='ساعت همیلتون', category = sub11, price=3250000, popular = True, description='ساعت همیلتون، ساخته شده در کشور سوئیس، وارد کننده: علی خردمند', image="images/products/watch men.jpg")
def init():
    cat1, ok = Category.objects.get_or_create(name='زنانه', img="images/profilepics/Capture.JPG")

    cat2, ok = Category.objects.get_or_create(name='مردانه',  img="images/profilepics/Capture.JPG")

    sub1, ok = Category.objects.get_or_create(name='کفش', img="images/profilepics/women-shoes.jpg")
    sub2, ok = Category.objects.get_or_create(name='لباس', img="images/profilepics/dress.jpg")
    sub3, ok = Category.objects.get_or_create(name='جواهرات', img="images/profilepics/necklace.jpg")
    sub4, ok = Category.objects.get_or_create(name='عطر', img="images/profilepics/perfume2.jpg")
    sub5, ok = Category.objects.get_or_create(name='ساعت', img="images/profilepics/women-watch.jpg")
    sub6, ok = Category.objects.get_or_create(name='کیف', img="images/profilepics/women-bag.jpg")
    sub7, ok = Category.objects.get_or_create(name='کفش', img="images/profilepics/shoes me.jpg")
    sub8, ok = Category.objects.get_or_create(name='کت و شلوار', img="images/profilepics/suit.jpg")
    sub9, ok = Category.objects.get_or_create(name='متعلقات', img="images/profilepics/tie.jpg")
    sub10, ok = Category.objects.get_or_create(name='عطر', img="images/profilepics/perfume5.jpg")
    # sub11, ok = Category.objects.get_or_create(name='ساعت', img="images/profilepics/men_wathc.jpg")
    sub12, ok = Category.objects.get_or_create(name='کیف', img="images/profilepics/bag_man.jpg")

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

    # pro1, ok = Product.objects.get_or_create(name='ساعت همیلتون', category = sub11, price=3250000, popular = True, description='ساعت همیلتون، ساخته شده در کشور سوئیس، وارد کننده: علی خردمند', image="images/products/watch men.jpg")
    pro2, ok = Product.objects.get_or_create(name='عطر گوچی', category=sub4, price=325000, popular=True, description='عطر گوچی 100 میلی لیتری مناسب برای خانم ها در تمامی سنین', image="images/products/perfume3.jpg")
    pro3, ok = Product.objects.get_or_create(name='کفش ایروبلو', category=sub1, price=265000, popular=True, description='بگذارید راز بلندی قد شما همیشه بین خودتان و کفشتان باقی بماند!! کفش های پاشنه بلند ایروبلو', image="images/products/6.jpg")
    pro4, ok = Product.objects.get_or_create(name='ست مروارید', category=sub3, price=5036500, popular=True, description='برای آنان که قصد عروسی دارند!! ست مروارید با تخفیفی باورنکردنی', image="images/products/jewlry.jpg")

    com1, ok = Comment.objects.get_or_create(name='مریم', product=pro1,comment='خوشگله')
    com2, ok = Comment.objects.get_or_create(name='مریم', product=pro2,comment='خوشگله')
    com3, ok = Comment.objects.get_or_create(name='فرناز', product=pro1,comment='گنده است')

def init2():
    com4, ok = Comment.objects.get_or_create(name='علی', product=pro1,comment='دوستش داشتم')
    com5, ok = Comment.objects.get_or_create(name='هادی', product=pro1,comment='خوبه')

