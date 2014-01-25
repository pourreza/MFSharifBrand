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
from django.contrib.auth.models import User

from MFSharif.forms import DocumentForm
from MFSharif.forms import RegisterUser
# from StringIO import StringIO
# from django.http import HttpResponse
# import cairo

from MFSharif.models import *
from PIL import Image
import os
import tempfile
import re
# from chartit import DataPool, Chart
from chartit import PivotDataPool, PivotChart
import PyICU
import types

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
    # print("useeeeeeeeeeeeeeeeeeeeeeeeeeeeeeer")
    if len(User.objects.filter(username = request.user.username))>0:
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
    else:
        if not 'products' in request.session :
            print("vaa here injaaaaaaaaaaaa")
            request.session['products']=[]
            request.session['numbers']=[]
            product_ids = []
            product_names = []
            product_count = []
            product_unit =[]
            sum = 0
        else:
            pro = request.session['products']
            print (pro)
            product_ids = []
            product_names = []
            product_count = request.session['numbers']
            product_unit =[]
            sum = 0
            i = 0
            for pr in pro:
                product_ids.append(pr)
                print ("ta injaaa umadam")
                p = Product.objects.get(pk=pr)
                print("badesh")
                print(p)
                product_names.append(p.name)
                product_unit.append(p.unit)
                sum += product_count[i]*p.price
                i +=1
    response_data = {'result':1, 'product_ids':product_ids, 'product_names':product_names, 'product_count':product_count,'product_unit':product_unit, 'sum':sum}
    return HttpResponse(json.dumps(response_data, cls=DjangoJSONEncoder), content_type="application/json")

def removeCartProduct(request):
    usr = request.user
    if len(User.objects.filter(username = request.user.username))>0:
        marketbasket = MarketBasket.objects.filter(customer__user = usr,paid='not_paid')
        id = request.GET.get('id')

        pr = Product.objects.get(pk = id)
        marketbasket[0].remove_item(pr)
        sum = marketbasket[0].totalPrice
    else:
        id = request.GET.get('id')
        temp = request.session['products']
        temp2 = request.session['numbers']
        counter = 0
        index = 0
        for t in temp:
            if id==t:
                index = counter
            counter +=1
        if temp2[index]>1:
            temp2[index] -= 1
            request.session['numbers'] = temp2
        else:
            del temp[index]
            del temp2[index]
            request.session['products'] = temp
            request.session['numbers'] = temp2

        sum = 0
        counter = 0
        for t in temp:
            p = Product.objects.get(pk = t)
            sum += temp2[counter]*p.price
            counter += 1
    response_data = {'result':1, 'sum':sum}
    return HttpResponse(json.dumps(response_data, cls=DjangoJSONEncoder), content_type="application/json")

def addCartProduct(request):
    usr = request.user
    if len(User.objects.filter(username = request.user.username))>0:
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
    else:
        if not 'products' in request.session :
            print("vaa here injaaaaaaaaaaaa")
            request.session['products']=[]
            temp = request.session['products']
            temp.append(request.GET.get('id'))
            request.session['products'] = temp
            request.session['numbers']=[]
            temp2 = request.session['numbers']
            temp2.append(1)
            request.session['numbers']=temp2
            product_ids = [request.GET.get('id')]
            id = request.GET.get('id')
            product_names = [Product.objects.get(pk=id).name]
            product_count = [1]
            product_unit =[Product.objects.get(pk=id).unit]
            sum = Product.objects.get(pk=id).price
        else:
            id = request.GET.get('id')
            ids = request.session['products']
            exist = False
            index = -1
            counter = 0
            for i in ids:
                if id==i:
                    exist = True
                    index= counter
                counter +=1
            if exist:
                temp = request.session['numbers']
                temp[index] += 1
                request.session['numbers']  = temp
                product_ids = request.session['products']
                product_count = request.session['numbers']
                product_names = []
                product_unit = []
                sum = 0
                counter = 0
                for x in product_ids:
                    p = Product.objects.get(pk=x)
                    product_names.append(p.name)
                    product_unit.append(p.unit)
                    sum += product_count[counter]*p.price
                    counter +=1
            else:
                temp = request.session['numbers']
                temp.append(1)
                request.session['numbers'] = temp
                temp2 = request.session['products']
                temp2.append(id)
                request.session['products'] = temp2
                product_ids = request.session['products']
                product_count = request.session['numbers']
                product_names = []
                product_unit = []
                sum = 0
                counter = 0
                for x in product_ids:
                    p = Product.objects.get(pk=x)
                    product_names.append(p.name)
                    product_unit.append(p.unit)
                    sum += product_count[counter]*p.price
                    counter +=1

    response_data = {'result':1, 'product_ids':product_ids, 'product_names':product_names, 'product_count':product_count,'product_unit':product_unit, 'sum':sum}
    return HttpResponse(json.dumps(response_data, cls=DjangoJSONEncoder), content_type="application/json")
def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K


def buyProducts(request):
    usr = request.user
    if len(User.objects.filter(username = request.user.username))>0:
        marketbasket = MarketBasket.objects.filter(customer__user = usr,paid='not_paid')
        if len(marketbasket)>0:
            products = []
            prs = marketbasket[0].productList.all()
            if len(prs)>0:
                mr = marketbasket[0]
                product_names = []
                for pr in prs:
                    product_names.append(pr.name)
                collator = PyICU.Collator.createInstance(PyICU.Locale('fa_IR.UTF-8'))
                print(product_names)
                product_names = sorted (product_names, key = cmp_to_key(collator.compare))
                print("badesh")
                print(product_names)

                for pn in product_names:
                    mkp = MarketBasket_Product.objects.get(basket = mr, product__name=pn)
                    products.append((mkp.product,mkp.number))
                total = marketbasket[0].totalPrice
                context = {'products':products, 'sum':total, 'usr':True}
            else:
                context = {'error':'سبد خرید خالیست!'}
        else:
            context = {'error':'سبد خرید خالیست!'}
    else:
        if not 'products' in request.session :
            request.session['products']=[]
            request.session['numbers']=[]
            product_ids = []
            product_names = []
            product_count = []
            product_unit =[]
            sum = 0
            context = {'error':'سبد خرید خالیست!'}
        else:
            pro = request.session['products']
            print (pro)
            product_ids = []
            product_names = []
            product_count = request.session['numbers']
            product_unit =[]
            prods = []
            sum = 0
            i = 0
            for pr in pro:
                product_ids.append(pr)
                p = Product.objects.get(pk=pr)
                print(p)
                print("sabaad")

                print(p)
                product_names.append(p.name)
                product_unit.append(p.unit)
                sum += product_count[i]*p.price
                prods.append((p,product_count[i]))
                i +=1
            print (prods)
            context = {'products':prods, 'sum':sum , 'usr':False}
            if len(prods)==0:
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
    if len(User.objects.filter(username = request.user.username))>0:
        if (User.objects.get(username= request.user.username).has_perm('MFSharif.is_customer')):
            usr = False
        else:
            usr = True
    else:
        usr = True
    context={'product':pro, 'comments':comments, 'dates':dates, 'similars': similars, 'recoms': recoms, 'URL':'ProductDetail', 'usr':usr}
    return render(request,'ProductDetail.html', context)

def addComment(request):
    global image_uploaded
    image_uploaded = False
    msg = request.GET.get('message')
    pro_id = request.GET.get('pro_id')
    print("message")
    prd = Product.objects.get(pk=pro_id)
    usr = request.user
    mfuser = MFUser.objects.get(user = usr)
    cm = Comment.objects.get_or_create(comment=msg, customer=mfuser, product=prd)
    print("injaaaaa")

    comments = Comment.objects.filter(product=prd).order_by('-date')
    #print(comments[0].comment)
    cm = []
    nms = []
    dt = []
    tm =[]
    for comment in comments:
        cm.append(comment.comment)
        nms.append(comment.customer.user.first_name)
        dt.append(comment.date.date())
        # tm.append(comment.date.time())

    response_data = {'result':1, 'comments':cm, 'names':nms, 'dates':dt, 'times':tm}
    # response_data = {'result':1, 'comments':comments}
    return HttpResponse(json.dumps(response_data, cls=DjangoJSONEncoder), content_type="application/json")


def loadsearch(request):
    global image_uploaded
    image_uploaded = False
    if len(User.objects.filter(username = request.user.username))>0:
        if (User.objects.get(username= request.user.username).has_perm('MFSharif.is_customer')):
            usr = False
        else:
            usr = True
    else:
        usr = True

    context = {'URL':'search','usr':usr}
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
    if len(User.objects.filter(username = request.user.username))>0:
        if (User.objects.get(username= request.user.username).has_perm('MFSharif.is_customer')):
            usr = False
        else:
            usr = True
    else:
        usr = True
    response_data = {"page": whichpage, 'pageSize': len(items), 'totalResults': totalresults, 'productList': responselist}
    recoms = Product.objects.filter(recommended = True)
    context = { 'recoms':recoms, 'URL': 'search.html', 'usr':usr}
    render(request,'search.html', context)

    return HttpResponse(json.dumps(response_data), content_type="application/json")


def into_search(request, category, search_str):
    global image_uploaded
    image_uploaded = False
    recoms = Product.objects.filter(recommended = True)

    if len(User.objects.filter(username = request.user.username))>0:
        if (User.objects.get(username= request.user.username).has_perm('MFSharif.is_customer')):
            usr = False
        else:
            usr = True
    else:
        usr = True
    context = {'p_category_': category, 'p_search_str_': search_str, 'recoms': recoms, 'URL': 'search', 'usr':usr};
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

def edit_pro(request, pro_id):
    pr = Product.objects.get(pk = pro_id)
    context={'pr':pr}
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
        m = str(len(Product.objects.all())+1)
        strnm = "images/products/"+m+".JPEG"
        print("strnm")
        print(strnm)
    except Exception as num:
        print("exe dige injaaa ??!!!")
        print(num)

    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        script_dir2 = os.path.dirname(script_dir)

        m = str(len(Product.objects.all())+1)
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
        usr = request.user
        mfuser = MFUser.objects.get(user = usr)
        pr = Product.objects.get_or_create(name=nm, category=cat, price=prc, description=des, image= strnm, salesman = mfuser)
    except Exception as num:
        print("tu save prodcut ")
        print(num)

    prsss = Product.objects.all().last()
    print(prsss.name)
    print(prsss.pk)
    print(prsss.image.url)

    response_data = {'result':1}
    return HttpResponse(json.dumps(response_data, cls=DjangoJSONEncoder), content_type="application/json")

def submit_edit_product(request):
    global number_crop
    print("injaaaaaaaaaaaaaaaaaaaaaaaaaaaa hastaaaaaaaaaaaaaam")
    nm = request.POST["name"]
    print("name")
    ctid = request.POST["category"]
    cat = Category.objects.get(pk=ctid)
    pr = request.POST["price"]
    product_id = request.POST["id"]
    print("pr")
    prc = int(pr)

    des = request.POST["description"]
    product = Product.objects.get(pk=product_id)
    #

    try:
        handle_uploaded_file(request.FILES["files"])
        script_dir = os.path.dirname(os.path.abspath(__file__))
        script_dir2 = os.path.dirname(script_dir)
        m = str(len(Product.objects.all()))
        st2 = "media\images\\test\\"+ m + ".JPEG"
        im = Image.open(st2)

        # script_dir = os.path.dirname(os.path.abspath(__file__))
        # script_dir2 = os.path.dirname(script_dir)
        # print(script_dir2)
        # tr = os.path.join(script_dir2, 'media\images\products')
        # print(tr)
        # print(strr[16:])
        # ttr = os.path.join(tr,strr[16:])
        # print(ttr)
        # script_dir = os.path.dirname(os.path.abspath(__file__))
        # script_dir2 = os.path.dirname(script_dir)
        # m = str(len(Product.objects.all()))
            # st2 = "media\images\\test\\"+ m + ".JPEG"

        # im = Image.open(st2)

    except Exception as inst:
        im = Image.open(product.image)
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
        m = str(product_id)
        strnm = "images/products/"+m+".JPEG"
        print("strnm")
        print(strnm)
    except Exception as num:
        print("exe dige injaaa ??!!!")
        print(num)

    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        script_dir2 = os.path.dirname(script_dir)

        m = str(product_id)
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
        print("Editttttttttttttttttttttttttttt Product")
        pr = Product.objects.get(pk=product_id)
        print(pr)
        pr.name = nm
        pr.image = strnm
        pr.price = prc
        pr.description = des
        pr.category = cat
        pr.save()
        # pr = Product.objects.get_or_create(name=nm, category=cat, price=prc, description=des, image= strnm)
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
    usr = request.user
    mfuser = MFUser.objects.get(user = usr)
    my_pros = Product.objects.filter(salesman = mfuser)
    market_products = []
    sum = 0
    for pr in my_pros:
        mrb = MarketBasket_Product.objects.filter(product=pr)
        for m in mrb:
            if m.basket.paid=='paid':
                market_products.append((m.basket, m.product, m.number))
                print(m.product.name)
                print(m.product.price)
                sum +=(m.number * m.product.price)
                print("summmmmm")
                print(sum)
    print("market product")
    market_products = sorted(market_products, key = (lambda x: x[0].lastModified))

    final_product = []
    i = 1
    while i<len(market_products):
        prss_name = []
        prss_name.append(market_products[i-1][1].name)
        time = market_products[i-1][0].lastModified
        print("last i")
        while i<len(market_products) and market_products[i-1][0].lastModified == market_products[i][0].lastModified:
            print(market_products[i][1])
            prss_name.append(market_products[i][1].name)
            i += 1
        print("i")
        print(i)
        collator = PyICU.Collator.createInstance(PyICU.Locale('fa_IR.UTF-8'))
        l = [z for z in sorted(["نیم بوت","کفش آل"], key=cmp_to_key(collator.compare))]
        print(l)
        print (l[0])
        collator = PyICU.Collator.createInstance(PyICU.Locale('fa_IR.UTF-8'))
        print("ghablesh")
        print(prss_name)
        prss_name = sorted(prss_name, key=cmp_to_key(collator.compare))
        print(prss_name[0])
        print("pas kushiii ")
        print(prss_name[0])
        prss = []
        for m in prss_name:
            bs = MarketBasket.objects.get(lastModified=time)
            x = MarketBasket_Product.objects.get(basket=bs , product__name=m)
            print ("x got")
            print(x.product)
            prss.append((x.basket,x.product,x.number))
        i +=1
        print(prss)
        final_product.extend(prss)

    context={'URL':'transactions', 'market_products':final_product , 'sum':sum}
    return render(request,"transactions.html",context)

# def chart_report(request):
#     usr = request.user
#     mfuser = MFUser.objects.get(user = usr)
#     pros = Product.objects.filter(salesman=mfuser).order_by('name')
#     counter = 1
#     for pr in pros:
#         num = 0
#         mkb = MarketBasket_Product.objects.filter(product=pr , basket__paid='paid')
#         for mm in mkb:
#             num += mm.number
#         namee = pr.name
#         ChartData.objects.get_or_create(status=namee,quantity=num)
#         counter += 1
#     # try:
#     #     unicode = unicode
#     # except NameError:
#     #     # 'unicode' is undefined, must be Python 3
#     #     str = str
#     #     unicode = str
#     #     bytes = bytes
#     #     basestring = (str,bytes)
#     # else:
#     #     str = str
#     #     # 'unicode' exists, must be Python 2
#     #     unicode = unicode
#     #     bytes = str
#     #     basestring = basestring
#     ds = DataPool(
#         series=
#         [{'options': {
#             'source': ChartData.objects.all()},
#           'terms': [
#               'status',
#               'quantity']}
#         ])
#
#     cht = Chart(
#         datasource = ds,
#         series_options =
#         [{'options':{
#             'type': 'column',
#             'stacking': False},
#           'terms':{
#               'status': [
#                   'quantity']
#           }}])
#
#     return render(request,'ChartReport.html', {'chart':pivcht})

def edit_products(request):
    usr = request.user
    mfuser = MFUser.objects.get(user = usr)
    my_pros = Product.objects.filter(salesman = mfuser)
    names = []
    for p in my_pros:
        names.append(p.name)

    collator = PyICU.Collator.createInstance(PyICU.Locale('fa_IR.UTF-8'))
    names = sorted(names, key = cmp_to_key(collator.compare))

    final_products = []
    for n in names:
        p = Product.objects.get(salesman = mfuser, name=n)
        final_products.append(p)

    context={'URL':'EditProducts', 'products':final_products}
    return render(request,"EditProducts.html",context)

def removeProduct(request):
    usr = request.user
    id = request.GET.get('id')
    mfuser = MFUser.objects.get(user = usr)
    Product.objects.get(pk=id).delete()

    response_data = {'result':1}
    return HttpResponse(json.dumps(response_data, cls=DjangoJSONEncoder), content_type="application/json")

def UserEnter(request):
    user_n = request.POST["username"]
    pass_w = request.POST['password']

    #print ('user_n: ',user_n)

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

def ShowProfile(request):
    return render(request, 'Profile.html', {})

def ChangeInfo(request):
    username_ = request.POST['username']
    first_name_ = request.POST['first_name']
    last_name_ = request.POST['last_name']
    phone_ = request.POST['phone']
    postal_code_ = request.POST['postal_code']
    password_ = request.POST['password']
    address_ = request.POST['address']

    user = User.objects.get(username__exact = username_)
    user.set_password(password_)
    user.first_name = first_name_
    user.last_name = last_name_
    user.mfuser.phone = phone_
    user.mfuser.postal_code = postal_code_
    user.mfuser.address = address_
    user.save()
    user.mfuser.save()

    return HttpResponseRedirect('/Profile')