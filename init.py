# -*- coding: utf-8 -*
from MFSharif.models import *
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType

def init():

    ct = ContentType.objects.get_for_model(MFUser)
    perm1, ok = Permission.objects.get_or_create(content_type = ct, codename = 'is_customer', name = 'Can act like a normal customer')
    perm2, ok = Permission.objects.get_or_create(content_type = ct, codename = 'is_salesman', name = 'Can act like a salesman')

    user1, ok =User.objects.get_or_create(username = 'maryam', first_name = 'مریم', last_name = 'پوررضا', email = 'mm.pourreza@gmail.com')
    user1.set_password('123')
    user1.save()
    user2, ok =User.objects.get_or_create(username = 'farnaz', first_name = 'فرناز', last_name = 'جهان بخش', email = 'farnaz.jahanbakhsh92@gmail.com')
    user2.set_password('123')
    user2.save()
    user3, ok =User.objects.get_or_create(username = 'ali', first_name = 'علی', last_name = 'خردمند', email = 'a.i.kheradmand@gmail.com')
    user3.set_password('123')
    user3.save()
    user4, ok =User.objects.get_or_create(username = 'atiye', first_name = 'عطیه', last_name = 'اشعری', email = 'atiyeashari@gmail.com')
    user4.set_password('123')
    user4.save()

    customer1, ok = MFUser.objects.get_or_create(postal_code = '1234567890', address = 'بلوار ارشاد-خیابان وحدت - نبش وحدت 6- مجتمع مسکونی یاس', phone = '66', city = 'مشهد', user= user1)

    customer2, ok = MFUser.objects.get_or_create(user=user2,postal_code = '1234567890', address = 'نزدیک باغ ارم', phone = '66', city = 'شیراز')

    customer3, ok = MFUser.objects.get_or_create(user = user3,postal_code = '1234567890', address = 'خیابان پل خواجو :-؟؟', phone = '66', city = 'اصفهان')

    customer4, ok = MFUser.objects.get_or_create(user = user4,postal_code = '1234567890', address = 'بلوار اول، خیابان دوم', phone = '66', city = 'کرج')

    user1.user_permissions.add(perm2)
    user3.user_permissions.add(perm2)

    user2.user_permissions.add(perm1)
    user4.user_permissions.add(perm1)

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

    pro1, ok = Product.objects.get_or_create(name='ساعت همیلتون', category = sub11, price=3250000, popular = True, recommended= False, description='ساعت همیلتون، ساخته شده در کشور سوئیس، وارد کننده: علی خردمند', image="images/products/watch men.jpg", salesman=customer3)
    pro2, ok = Product.objects.get_or_create(name='عطر گوچی', category=sub4, price=325000, popular=True, recommended = False, description='عطر گوچی 100 میلی لیتری مناسب برای خانم ها در تمامی سنین', image="images/products/perfume4.jpg", salesman=customer3)
    pro3, ok = Product.objects.get_or_create(name='کفش ایروبلو', category=sub1, price=265000, popular=True, recommended = False, description='بگذارید راز بلندی قد شما همیشه بین خودتان و کفشتان باقی بماند!! کفش های پاشنه بلند ایروبلو', image="images/products/8.jpg", salesman=customer3)
    pro4, ok = Product.objects.get_or_create(name='ست مروارید', category=sub3, price=5036500, popular=True, recommended = False, description='برای آنان که قصد عروسی دارند!! ست مروارید با تخفیفی باورنکردنی', image="images/products/pearl.jpg", salesman=customer3)
    pro5, ok = Product.objects.get_or_create(name='انگشتر پاپیون', category=sub3, price=15036500, popular=False, recommended = False, description='انگشتر الماس بسیار شیک برای آنان که پول دارند', image="images/products/3_00.jpg", salesman=customer3)
    pro6, ok = Product.objects.get_or_create(name=' دستبند برگ زرد', category=sub3, price=638500, popular=False, recommended = True, description='اجازه دهید پاییز همیشه همراهتان باشد', image="images/products/3_1.jpg", salesman=customer3)
    pro7, ok = Product.objects.get_or_create(name='دستبند فرد و جورج', category=sub3, price=69000, popular=False, recommended = True, description='برای آنان که قسم خورده‌اند قصد انجام کار خوبی ندارند', image="images/products/3_3.jpg", salesman=customer1)
    pro8, ok = Product.objects.get_or_create(name='گوشواره های میناکاری شده', category=sub3, price=69000, popular=False, recommended = True, description='بهترین و رنگارنگ‌ترین هدیه برای دوستتان', image="images/products/3_02.jpg", salesman=customer1)
    pro9, ok = Product.objects.get_or_create(name='گردنبند گردن سوراخ کن', category=sub3, price=70000, popular=False, recommended = True, description='برای آنان که مشکلی با سوراخی گردن خود ندارند', image="images/products/3_6.jpg", salesman=customer1)
    pro10, ok = Product.objects.get_or_create(name='پیراهن خیلی صورتی', category=sub2, price=170000, popular=False, recommended = False, description='نکته‌ی مثبت در مورد این پیراهن این است که نه صورتی آدامسی است نه باربی‌ای', image="images/products/4_12.jpg", salesman=customer1)
    pro11, ok = Product.objects.get_or_create(name='پالتو ومپایری', category=sub2, price=230000, popular=False, recommended = False, description='برای علاقه‌مندان به ابهت یک ومپایر', image="images/products/4_5.jpg", salesman=customer1)
    pro12, ok = Product.objects.get_or_create(name='کفش آل استار', category=sub1, price=230000, popular=False, recommended = False, description='در طرح‌ها و رنگ‌های مختلف متناسب با سلیقه‌ی شما', image="images/products/1_02.jpg", salesman=customer1)
    pro13, ok = Product.objects.get_or_create(name='بوت خیلی بلند', category=sub1, price=320000, popular=False, recommended = False, description='این بوت هم خودش بلند است هم کمک می‌کند شما بلند به نظر برسید', image="images/products/1_03.jpg", salesman=customer1)
    pro14, ok = Product.objects.get_or_create(name='سندل خیلی ظریف', category=sub1, price=140000, popular=False, recommended = False, description='این سندل هم خودش ظریف است هم کمک می‌کند شما ظریف به نظر برسید', image="images/products/1_04.jpg", salesman=customer1)
    pro15, ok = Product.objects.get_or_create(name='نیم بوت قهوه ای', category=sub1, price=180000, popular=False, recommended = False, description='این نیم‌بوت بسیار گرم و بسیار قهوه‌ایست', image="images/products/1_7.jpg", salesman=customer1)
    pro16, ok = Product.objects.get_or_create(name='پیراهن گل منگلی', category=sub2, price=240000, popular=False, recommended = False, description='با پوشیدن این پیراهن شما به گل‌منگلی‌ترین خانم مجلس تبدیل خواهید شد.', image="images/products/4_16.jpg", salesman=customer1)
    pro17, ok = Product.objects.get_or_create(name='تی شرت تیرخوردگی', category=sub2, price=140000, popular=False, recommended = False, description='یک تی‌شرت زیبا برای آنان که مرض دارند.', image="images/products/4_9.jpg", salesman=customer1)
    pro18, ok = Product.objects.get_or_create(name='عطر بولگاری ', category=sub4, price=425000, popular= False, recommended = False, description='عطر بولگاری بسیار خوشبو مناسب برای بعضی سنین', image="images/products/4_03.jpg", salesman=customer3)
    pro19, ok = Product.objects.get_or_create(name='عطر خاویار قرمز ', category=sub4, price=250000, popular= False, recommended = False, description='بهترین هدیه برای آن کس که دوستش دارید', image="images/products/4_01.jpg", salesman=customer3)
    pro20, ok = Product.objects.get_or_create(name='عطر چوب ', category=sub4, price=250000, popular= False, recommended = False, description='مناسب برای آنان که از این دنیا فقط یک صندلی چوبی می‌خواهند', image="images/products/4_02.jpg", salesman=customer3)
    pro21, ok = Product.objects.get_or_create(name='ساعت عهد شاه وزوزک ', category = sub11, price=2750000, popular = False, recommended= False, description='گذشته‌ها را به خاطر بیاورید. زمان در دستان شماست', image="images/products/11_1.jpg", salesman=customer3)
    pro22, ok = Product.objects.get_or_create(name='ساعت بنددراز', category = sub11, price=120000, popular = False, recommended= False, description='بند بسیار بلند این ساعت چشم همگان را به خود خیره خواهد ساخت', image="images/products/11_2.jpg", salesman=customer3)
    pro23, ok = Product.objects.get_or_create(name=' ساعت گیکی', category = sub11, price=2080000, popular = False, recommended= False, description='ساعت پیشرفته مناسب برای گیک‌ها در تمامی سنین', image="images/products/11_3.jpg", salesman=customer3)
    #pro24, ok = Product.objects.get_or_create(name='  متعل یک', category = sub9, price=2080000, popular = False, recommended= False, description='ساعت پیشرفته مناسب برای گیک‌ها در تمامی سنین', image="images/products/3_3.jpg")
    #pro25, ok = Product.objects.get_or_create(name='  متعل دو', category = sub9, price=2080000, popular = False, recommended= False, description='ساعت پیشرفته مناسب برای گیک‌ها در تمامی سنین', image="images/products/1_7.jpg")
    #pro26, ok = Product.objects.get_or_create(name='  متعل سه', category = sub9, price=2080000, popular = False, recommended= False, description='ساعت پیشرفته مناسب برای گیک‌ها در تمامی سنین', image="images/products/4_03.jpg")
    #pro27, ok = Product.objects.get_or_create(name='  کت شلوار یک', category = sub8, price=2080000, popular = False, recommended= False, description='ساعت پیشرفته مناسب برای گیک‌ها در تمامی سنین', image="images/products/3_3.jpg")
    #pro28, ok = Product.objects.get_or_create(name='  کت شلوار دو', category = sub8, price=2080000, popular = False, recommended= False, description='ساعت پیشرفته مناسب برای گیک‌ها در تمامی سنین', image="images/products/1_7.jpg")
    #pro29, ok = Product.objects.get_or_create(name='کت شلوار سه', category = sub8, price=2080000, popular = False, recommended= False, description='ساعت پیشرفته مناسب برای گیک‌ها در تمامی سنین', image="images/products/4_03.jpg")
    #pro30, ok = Product.objects.get_or_create(name='عطر یک', category = sub10, price=2080000, popular = False, recommended= False, description='ساعت پیشرفته مناسب برای گیک‌ها در تمامی سنین', image="images/products/3_3.jpg")
    #pro31, ok = Product.objects.get_or_create(name='عطردو', category = sub10, price=2080000, popular = False, recommended= False, description='ساعت پیشرفته مناسب برای گیک‌ها در تمامی سنین', image="images/products/1_7.jpg")
    #pro32, ok = Product.objects.get_or_create(name='عطر سه', category = sub10, price=2080000, popular = False, recommended= False, description='ساعت پیشرفته مناسب برای گیک‌ها در تمامی سنین', image="images/products/4_03.jpg")
    #pro33, ok = Product.objects.get_or_create(name=' کفش یک', category = sub7, price=2080000, popular = False, recommended= False, description='ساعت پیشرفته مناسب برای گیک‌ها در تمامی سنین', image="images/products/3_3.jpg")
    #pro34, ok = Product.objects.get_or_create(name='کفش دو', category = sub7, price=2080000, popular = False, recommended= False, description='ساعت پیشرفته مناسب برای گیک‌ها در تمامی سنین', image="images/products/1_7.jpg")
    #pro35, ok = Product.objects.get_or_create(name=' کفش سه', category = sub7, price=2080000, popular = False, recommended= False, description='ساعت پیشرفته مناسب برای گیک‌ها در تمامی سنین', image="images/products/4_03.jpg")
    #pro36, ok = Product.objects.get_or_create(name=' کیف یک', category = sub12, price=2080000, popular = False, recommended= False, description='ساعت پیشرفته مناسب برای گیک‌ها در تمامی سنین', image="images/products/3_3.jpg")
    #pro37, ok = Product.objects.get_or_create(name=' کیف دو', category = sub12, price=2080000, popular = False, recommended= False, description='ساعت پیشرفته مناسب برای گیک‌ها در تمامی سنین', image="images/products/1_7.jpg")
    #pro38, ok = Product.objects.get_or_create(name='کیف سه', category = sub12, price=2080000, popular = False, recommended= False, description='ساعت پیشرفته مناسب برای گیک‌ها در تمامی سنین', image="images/products/4_03.jpg")
    #pro39, ok = Product.objects.get_or_create(name='  ساعت یک', category = sub5, price=2080000, popular = False, recommended= False, description='ساعت پیشرفته مناسب برای گیک‌ها در تمامی سنین', image="images/products/3_3.jpg")
    #pro40, ok = Product.objects.get_or_create(name='ساعت دو ', category = sub5, price=2080000, popular = False, recommended= False, description='ساعت پیشرفته مناسب برای گیک‌ها در تمامی سنین', image="images/products/1_7.jpg")
    #pro41, ok = Product.objects.get_or_create(name='ساعت۳', category = sub5, price=2080000, popular = False, recommended= False, description='ساعت پیشرفته مناسب برای گیک‌ها در تمامی سنین', image="images/products/4_03.jpg")
    #pro42, ok = Product.objects.get_or_create(name=' کیف یک', category = sub6, price=2080000, popular = False, recommended= False, description='ساعت پیشرفته مناسب برای گیک‌ها در تمامی سنین', image="images/products/3_3.jpg")
    #pro43, ok = Product.objects.get_or_create(name=' کیف دو', category = sub6, price=2080000, popular = False, recommended= False, description='ساعت پیشرفته مناسب برای گیک‌ها در تمامی سنین', image="images/products/1_7.jpg")
    #pro44, ok = Product.objects.get_or_create(name='کیف سه', category = sub6, price=2080000, popular = False, recommended= False, description='ساعت پیشرفته مناسب برای گیک‌ها در تمامی سنین', image="images/products/4_03.jpg")
    #
    #
    #



    p1, ok = PopularProducts.objects.get_or_create(product = pro1, image="images/products/image.png")
    p2, ok = PopularProducts.objects.get_or_create(product = pro2, image="images/products/perfume3.jpg")
    p3, ok = PopularProducts.objects.get_or_create(product = pro3, image="images/products/6.jpg")
    p4, ok = PopularProducts.objects.get_or_create(product = pro4, image="images/products/jewlry.jpg")


    com1, ok = Comment.objects.get_or_create(customer=customer2, product=pro1,comment='خوشگله')
    com2, ok = Comment.objects.get_or_create(customer=customer4, product=pro2,comment='خوشگله')
    com3, ok = Comment.objects.get_or_create(customer=customer2, product=pro1,comment='گنده است')
    com4, ok = Comment.objects.get_or_create(customer=customer4, product=pro1,comment='دوستش داشتم')
    com5, ok = Comment.objects.get_or_create(customer=customer2, product=pro1,comment='خوبه')





