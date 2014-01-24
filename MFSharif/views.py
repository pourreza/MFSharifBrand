import json

from django.shortcuts import render
from django.core.paginator import Paginator
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import logout
from django.utils.itercompat import product

from MFSharif.forms import DocumentForm
from MFSharif.forms import RegisterUser

from MFSharif.models import *
from PIL import Image
import os
import tempfile
import re


image_uploaded = False
number_crop = 0

# Create your views here.
def index(request):
    print(request.user)
    global image_uploaded
    image_uploaded = False
    cat_women = Category.objects.filter(name='زنانه')
    cat_men = Category.objects.filter(name='مردانه')

    subs1 = SubCats.objects.filter(category=cat_women)
    subs2 = SubCats.objects.filter(category=cat_men)
    women_items = []
    for item in subs1:
        women_items.append(item.subcategory)

    men_items = []
    for item in subs2:
        men_items.append(item.subcategory)

    pro = PopularProducts.objects.all()
    recoms = Product.objects.filter(recommended = True)

    context = {'men_items':men_items, 'women_items':women_items, 'products':pro, 'recoms': recoms, 'URL': ''}
    return render(request, 'base.html', context)

def cartProducts(request):
    usr = request.user
    marketbasket = MarketBasket.objects.filter(customer__user = usr,paid='not_paid')
    print(marketbasket)
    if marketbasket:
        prs = marketbasket[0].productList.all()
    else:
        mfuser = MFUser.objects.get(user = usr)
        MarketBasket.createForCustomer(mfuser)
        marketbasket = MarketBasket.objects.filter(customer=mfuser,paid='not_paid')
        prs = []

    product_ids = []
    product_names = []
    product_count = []
    product_unit = []
    for pr in prs:
        mr = marketbasket[0]
        product_ids.append(pr.pk)
        product_names.append(pr.name)
        product_unit.append(pr.unit)
        num = MarketBasket_Product.objects.get(basket = mr, product=pr).number
        product_count.append(num)

    if marketbasket:
        sum = marketbasket[0].totalPrice
    else:
        sum = 0
    response_data = {'result':1, 'product_ids':product_ids, 'product_names':product_names, 'product_count':product_count,'product_unit':product_unit, 'sum':sum}
    return HttpResponse(json.dumps(response_data, cls=DjangoJSONEncoder), content_type="application/json")

def removeCartProduct(request):
    usr = request.user
    marketbasket = MarketBasket.objects.filter(customer__user = usr,paid='not_paid')
    id = request.GET.get('id')

    pr = Product.objects.get(pk = id)
    marketbasket[0].remove_item(pr)
    sum = marketbasket[0].totalPrice

    response_data = {'result':1, 'sum':sum}
    return HttpResponse(json.dumps(response_data, cls=DjangoJSONEncoder), content_type="application/json")

def addCartProduct(request):
    usr = request.user
    marketbasket = MarketBasket.objects.filter(customer__user = usr,paid='not_paid')
    id = request.GET.get('id')
    pr = Product.objects.get(pk=id)
    mr = marketbasket[0]
    num = MarketBasket_Product.objects.filter(basket=mr,product=pr)
    if len(num)>0:
        n = num[0].number
        num[0].number = n+1
        num[0].save()

    marketbasket[0].add_item(pr)
    marketbasket[0].updateItems()

    prs = marketbasket[0].productList.all()
    product_ids = []
    product_names = []
    product_count = []
    product_unit = []

    for pr in prs:
        product_ids.append(pr.pk)
        product_names.append(pr.name)
        product_unit.append(pr.unit)
        num = MarketBasket_Product.objects.get(basket = mr, product=pr).number
        print(num)
        product_count.append(num)

    sum = marketbasket[0].totalPrice
    response_data = {'result':1, 'product_ids':product_ids, 'product_names':product_names, 'product_count':product_count,'product_unit':product_unit, 'sum':sum}
    return HttpResponse(json.dumps(response_data, cls=DjangoJSONEncoder), content_type="application/json")

def buyProducts(request):
    usr = request.user
    marketbasket = MarketBasket.objects.filter(customer__user = usr,paid='not_paid')
    if len(marketbasket)>0:
        products = []
        prs = marketbasket[0].productList.all()
        if len(prs)>0:
            mr = marketbasket[0]
            for pr in prs:
                num = MarketBasket_Product.objects.get(basket = mr, product=pr).number
                products.append((pr,num))
            total = marketbasket[0].totalPrice
            context = {'products':products, 'sum':total}
        else:
            context = {'error':'سبد خرید خالیست!'}
    else:
        context = {'error':'سبد خرید خالیست!'}
    return render(request, "BuyProducts.html", context)

def confirmBuy(request):
    usr = request.user
    marketbasket = MarketBasket.objects.filter(customer__user = usr,paid='not_paid')
    if len(marketbasket)>0:
        marketbasket[0].paid = 'paid'
        marketbasket[0].save()
    response_data = {'result':1, }
    return HttpResponse(json.dumps(response_data, cls=DjangoJSONEncoder), content_type="application/json")

def product_info(request, pro_id):
    global image_uploaded
    image_uploaded = False
    pid = int(pro_id)
    pro = Product.objects.filter(pk=pid)
    comments = Comment.objects.filter(product=pro).order_by('-date')
    dates = []
    for comment in comments:
        dates.append(comment.date.date())

    proches = Product.objects.filter(category = pro[0].category)
    proches = proches.exclude(pk = pid)

    recoms = Product.objects.filter(recommended = True)


    similars = []
    for i in range(3):
        if proches[i]:
            #print('proches:',proches[i])
            print('url:', proches[i].image.url)
            dic_el = {'category': proches[i].category, 'price': proches[i].price, 'id': proches[i].pk, 'name': proches[i].name, 'picUrl': proches[i].image.url }
            similars.append(dic_el)

    context={'product':pro, 'comments':comments, 'dates':dates, 'similars': similars, 'recoms': recoms, 'URL':'ProductDetail'}
    return render(request,'ProductDetail.html', context)

def addComment(request):
    global image_uploaded
    image_uploaded = False
    msg = request.GET.get('message')
    pro_id = request.GET.get('pro_id')
    nm = request.GET.get('name')

    prd = Product.objects.get(pk=pro_id)
    cm = Comment.objects.get_or_create(comment=msg, name=nm, product=prd)

    comments = Comment.objects.filter(product=prd).order_by('-date')
    #print(comments[0].comment)
    cm = []
    nms = []
    dt = []
    tm =[]
    for comment in comments:
        cm.append(comment.comment)
        nms.append(comment.name)
        dt.append(comment.date.date())
        # tm.append(comment.date.time())

    response_data = {'result':1, 'comments':cm, 'names':nms, 'dates':dt, 'times':tm}
    # response_data = {'result':1, 'comments':comments}
    return HttpResponse(json.dumps(response_data, cls=DjangoJSONEncoder), content_type="application/json")


def loadsearch(request):
    global image_uploaded
    image_uploaded = False
    context = {'URL':'search'}
    return render(request, 'search.html', context)


def items_wanted(request):
    global image_uploaded
    image_uploaded = False
    category_ = request.GET["category"]
    search_string = request.GET["search"]
    whichpage = request.GET["page"]
    page_size = request.GET["pageSize"]

    print("category_", category_)

    desired_cat = []
    desired_prod = []

    desired_cat = Category.objects.filter( pk = category_)

    desired_subcat = SubCats.objects.filter( category = desired_cat[0])

    from itertools import chain
    desired_cats = list(chain(desired_cat, desired_subcat))
    #print('desiredcats',desired_cats[0])
    #
    #print('in',len(Product.objects.filter(category = desired_cats[5])))


    if desired_subcat:
        for x in desired_subcat:
            if Product.objects.filter(category = x.subcategory):
                desired_prod = list(chain(Product.objects.filter(category = x.subcategory), desired_prod))
    else:
        if Product.objects.filter(category = desired_cat[0]):
            desired_prod = list(Product.objects.filter(category = desired_cat[0]))

    #if search_string:
    #    qset = Q()
    #    for term in search_string.split():
    #        qset |= Q(name__contains = term)
    #    desired_prod = desired_prod.filter(qset)
    #
    final_prod = []
    if search_string:
        for term in search_string.split():
            for elem in desired_prod:
                for i in elem.name.split():
                    if term == i:
                        final_prod.append(elem)
    else:
        print ("empty")
        final_prod = desired_prod


    if not page_size:
        page_size = 8

    paginator = Paginator(final_prod, page_size)

    if not whichpage:
        whichpage = 1

    print ('whichpage', whichpage)
    print('pagesize', page_size)


    items = paginator.page(whichpage)
    totalresults = len(final_prod)

    print('len(items)',len(items))

    responselist = []
    for elem in items:
        dic_el = {'category': category_, 'price': elem.price, 'id': elem.pk, 'name': elem.name, 'picUrl': elem.image.url }
        responselist.append(dic_el)

    #responselist_ult = []
    #for i in responselist:
    #    if i not in responselist_ult:
    #        responselist.append(i)

    response_data = {"page": whichpage, 'pageSize': len(items), 'totalResults': totalresults, 'productList': responselist}
    recoms = Product.objects.filter(recommended = True)
    context = { 'recoms':recoms, 'URL': 'search.html'}
    render(request,'search.html', context)

    return HttpResponse(json.dumps(response_data), content_type="application/json")


def into_search(request, category, search_str):
    global image_uploaded
    image_uploaded = False
    recoms = Product.objects.filter(recommended = True)
    context = {'p_category_': category, 'p_search_str_': search_str, 'recoms': recoms, 'URL': 'search'};
    return render(request, 'search.html', context)


def list_categories(request):
    global image_uploaded
    image_uploaded = False
    list_of_cats = Category.objects.all()
    categorylist = []
    for elem in list_of_cats:
        dic_el = {'name': elem.name, 'id': elem.pk}
        categorylist.append(dic_el)

    response_data = {'categoryList': categorylist}
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def upload_image(request):
    global image_uploaded
    image_uploaded = False
    print("tu upload image am")
    response_data = {'result':1}
    # response_data = {'result':1, 'comments':comments}
    return HttpResponse(json.dumps(response_data, cls=DjangoJSONEncoder), content_type="application/json")


def addProduct2(request):
    global image_uploaded
    global number_crop
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            image_uploaded = True
            newdoc = UploadedImage(image = request.FILES['docfile'])
            newdoc.save()
            return HttpResponseRedirect(reverse('MFSharif.views.addProduct'))
    else:
        form = DocumentForm()

    imageFiles = UploadedImage.objects.all()
    img = imageFiles.last()
    if image_uploaded == False:
        img = ''
    return render_to_response('AddProduct.html', {'images':img , 'form': form},context_instance=RequestContext(request))

def addProduct(request):
    context={'URL':'ManageProducts'}
    return render(request,'ManageProducts.html', context)

def edit_pro(request):
    context={'ProductEdit'}
    return render(request,'ProductEdit.html', context)

def handle_uploaded_file(f):
    print("in uploaded file")
    try:
        print(f.size)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        script_dir2 = os.path.dirname(script_dir)
        m = str(len(Product.objects.all()))
        st2 = "media\images\\test\\"+ m + ".JPEG"
        print(st2)
        tr = os.path.join(script_dir2, st2)
        with open(tr, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
    except Exception as num:
        print("chunks")
        print(num)


def submit_product(request):
    print("i'm hereeeeeeee")
    global number_crop
    nm = request.POST["name"]
    print("name")
    ctid = request.POST["category"]
    cat = Category.objects.get(pk=ctid)
    pr = request.POST["price"]
    print("pr")
    prc = int(pr)

    des = request.POST["description"]
    # print(request.POST["files"])
    handle_uploaded_file(request.FILES["files"])
    # try:
    # print(request.FILES["files"])
    # except Exception as num:
    #     print("in xata")
    #     print(num)

    # form = DocumentForm(request.POST, request.FILES)
    # print(form.is_valid())
    # strr = request.GET["picURL"]
    try:
        # script_dir = os.path.dirname(os.path.abspath(__file__))
        # script_dir2 = os.path.dirname(script_dir)
        # print(script_dir2)
        # tr = os.path.join(script_dir2, 'media\images\products')
        # print(tr)
        # print(strr[16:])
        # ttr = os.path.join(tr,strr[16:])
        # print(ttr)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        script_dir2 = os.path.dirname(script_dir)
        m = str(len(Product.objects.all()))
        st2 = "media\images\\test\\"+ m + ".JPEG"
        im = Image.open(st2)

    except Exception as inst:
        print(inst)

    try:
        x = request.POST["x1"]
        xx = int(x)
        y = request.POST["y1"]
        yy = int(y)
        w = request.POST["w"]
        ww = int(w)
        h = request.POST["h"]
        hh = int(h)
        width, height = im.size
        print(width)
        print(height)
        xx = (xx*width)/300
        ww = (ww*width)/300
        hh = (hh*height)/300
        yy = (yy*height)/300
        xx = int(xx)
        yy = int(yy)
        ww = int(ww)
        hh = int(hh)
        immm = im.crop((xx ,yy,ww,hh))
    except Exception as num:
        print("in cropping")
        print(num)

    try:
        m = str(len(Product.objects.all()))
        strnm = "images/products/"+m+".JPEG"
        print("strnm")
        print(strnm)
    except Exception as num:
        print("exe dige injaaa ??!!!")
        print(num)

    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        script_dir2 = os.path.dirname(script_dir)

        m = str(len(Product.objects.all()))
        st2 = "media\images\products\\"+ m + ".JPEG"
        tr = os.path.join(script_dir2, st2)
        temp_file = open(tr,"w")
    except Exception as num:
        print("tu open temp file ")
        print(num)

    try:
        immm.save(temp_file,format("JPEG"))
    except Exception as num:
        print("in save crop")
        print(num)

    try:
        print("new Product")
        pr = Product.objects.get_or_create(name=nm, category=cat, price=prc, description=des, image= strnm)
    except Exception as num:
        print("tu save prodcut ")
        print(num)

    prsss = Product.objects.all().last()
    print(prsss.name)
    print(prsss.pk)
    print(prsss.image.url)

    response_data = {'result':1}
    return HttpResponse(json.dumps(response_data, cls=DjangoJSONEncoder), content_type="application/json")

def transactions(request):
    context={'URL':'transactions'}
    return render(request,"transactions.html",context)

def edit_products(request):
    context={'URL':'EditProducts'}
    return render(request,"EditProducts.html",context)

#def regFormSent(request):
#    if request.method == 'POST':
#        form = RegisterUser(request.POST)
#        if form.is_valid():
#            username = form.cleaned_data['username']
#            first_name = form.cleaned_data['first_name']
#            last_name = form.cleaned_data['last_name']
#            email = form.cleaned_data['email']
#            password = form.cleaned_data['password']
#            #send email
#            return HttpResponseRedirect('/thanks/')
#
#    else:
#        form = RegisterUser()
#    return render(request, 'Register.html', {'form': form})


def UserEnter(request):
    user_n = request.POST["username"]
    pass_w = request.POST['password']

    print ('user_n: ',user_n)

    if user_n is '' or pass_w is '':
        custom_message= 'لطفاً تمامی فیلدها را پر کنید'
        response_data={'custom_message': custom_message, 'status':'moldy'}
        return HttpResponse(json.dumps(response_data), content_type="application/json")


    user = authenticate(username = user_n, password = pass_w)

    if user is not None:
        if user.is_active:
            login(request,user)
            custom_message= 'خوش آمدید'
            response_data={'custom_message': custom_message, 'status':'ok'}
            return HttpResponse(json.dumps(response_data), content_type="application/json")

        else:
            custom_message= 'کاربر غیرفعال است'
            response_data={'custom_message': custom_message, 'status':'moldy'}
            return HttpResponse(json.dumps(response_data), content_type="application/json")

    else:
       custom_message = 'کاربری با کلمه‌ی عبور وارد شده وجود ندارد'
       response_data={'custom_message': custom_message, 'status':'moldy'}
       return HttpResponse(json.dumps(response_data), content_type="application/json")




def UserExit(request):
    logout(request)
    return HttpResponse(json.dumps({}), content_type="application/json")

