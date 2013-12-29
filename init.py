# -*- coding: utf-8 -*
from MFSharif.models import *


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
    sub11, ok = Category.objects.get_or_create(name='ساعت', img="images/profilepics/men_wathc.jpg")
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

    pro1, ok = Product.objects.get_or_create(name='ساعت همیلتون', category = sub11, price=3250000, popular = True, recommended= False, description='ساعت همیلتون، ساخته شده در کشور سوئیس، وارد کننده: علی خردمند', image="images/products/watch men.jpg")
    pro2, ok = Product.objects.get_or_create(name='عطر گوچی', category=sub4, price=325000, popular=True, recommended = False, description='عطر گوچی 100 میلی لیتری مناسب برای خانم ها در تمامی سنین', image="images/products/perfume3.jpg")
    pro3, ok = Product.objects.get_or_create(name='کفش ایروبلو', category=sub1, price=265000, popular=True, recommended = False, description='بگذارید راز بلندی قد شما همیشه بین خودتان و کفشتان باقی بماند!! کفش های پاشنه بلند ایروبلو', image="images/products/6.jpg")
    pro4, ok = Product.objects.get_or_create(name='ست مروارید', category=sub3, price=5036500, popular=True, recommended = False, description='برای آنان که قصد عروسی دارند!! ست مروارید با تخفیفی باورنکردنی', image="images/products/jewlry.jpg")
    pro5, ok = Product.objects.get_or_create(name='انگشتر پاپیون', category=sub3, price=15036500, popular=False, recommended = False, description='انگشتر الماس بسیار شیک برای آنان که پول دارند', image="images/products/3_00.jpg")
    pro6, ok = Product.objects.get_or_create(name=' دستبند برگ زرد', category=sub3, price=638500, popular=False, recommended = True, description='اجازه دهید پاییز همیشه همراهتان باشد', image="images/products/3_1.jpg")
    pro7, ok = Product.objects.get_or_create(name='دستبند فرد و جورج', category=sub3, price=69000, popular=False, recommended = True, description='برای آنان که قسم خورده‌اند قصد انجام کار خوبی ندارند', image="images/products/3_3.jpg")
    pro8, ok = Product.objects.get_or_create(name='گوشواره‌های مینا کاری شده', category=sub3, price=69000, popular=False, recommended = True, description='بهترین و رنگارنگ‌ترین هدیه برای دوستتان', image="images/products/3_02.jpg")
    pro9, ok = Product.objects.get_or_create(name='گردنبند گردن سوراخ کن', category=sub3, price=70000, popular=False, recommended = True, description='برای آنان که مشکلی با سوراخی گردن خود ندارند', image="images/products/3_6.jpg")
    pro10, ok = Product.objects.get_or_create(name='پیراهن خیلی صورتی', category=sub2, price=170000, popular=False, recommended = False, description='نکته‌ی مثبت در مورد این پیراهن این است که نه صورتی آدامسی است نه باربی‌ای', image="images/products/4_12.jpg")
    pro11, ok = Product.objects.get_or_create(name='پالتو ومپایری', category=sub2, price=230000, popular=False, recommended = False, description='برای علاقه‌مندان به ابهت یک ومپایر', image="images/products/4_5.jpg")
    pro12, ok = Product.objects.get_or_create(name='کفش آل‌استار', category=sub1, price=230000, popular=False, recommended = False, description='در طرح‌ها و رنگ‌های مختلف متناسب با سلیقه‌ی شما', image="images/products/1_02.jpg")
    pro13, ok = Product.objects.get_or_create(name='بوت خیلی بلند', category=sub1, price=320000, popular=False, recommended = False, description='این بوت هم خودش بلند است هم کمک می‌کند شما بلند به نظر برسید', image="images/products/1_03.jpg")
    pro14, ok = Product.objects.get_or_create(name=' سندل خیلی ظریف', category=sub1, price=140000, popular=False, recommended = False, description='این سندل هم خودش ظریف است هم کمک می‌کند شما ظریف به نظر برسید', image="images/products/1_04.jpg")
    pro15, ok = Product.objects.get_or_create(name=' نیم بوت قهوه‌ای', category=sub1, price=180000, popular=False, recommended = False, description='این نیم‌بوت بسیار گرم و بسیار قهوه‌ایست', image="images/products/1_7.jpg")



    com1, ok = Comment.objects.get_or_create(name='مریم', product=pro1,comment='خوشگله')
    com2, ok = Comment.objects.get_or_create(name='مریم', product=pro2,comment='خوشگله')
    com3, ok = Comment.objects.get_or_create(name='فرناز', product=pro1,comment='گنده است')
    com4, ok = Comment.objects.get_or_create(name='علی', product=pro1,comment='دوستش داشتم')
    com5, ok = Comment.objects.get_or_create(name='هادی', product=pro1,comment='خوبه')



