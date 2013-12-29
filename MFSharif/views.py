from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.http import HttpResponse
from MFSharif.models import *


# Create your views here.
def index(request):
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

    pro = Product.objects.filter(popular=True)
    recoms = Product.objects.filter(recommended = True)

    context = {'men_items':men_items, 'women_items':women_items, 'products':pro, 'recoms': recoms}
    return render(request, 'base.html', context)

def product_info(request, pro_id):
    pid = int(pro_id)
    pro = Product.objects.filter(pk=pid)
    comments = Comment.objects.filter(product=pro).order_by('-date')
    dates = []
    for comment in comments:
        dates.append(comment.date.date())
    context={'product':pro, 'comments':comments, 'dates':dates}
    return render(request,'ProductDetail.html', context)

def addComment(request):
    msg = request.GET.get('message')
    pro_id = request.GET.get('pro_id')
    nm = request.GET.get('name')

    prd = Product.objects.get(pk=pro_id)
    cm = Comment.objects.get_or_create(comment=msg, name=nm, product=prd)

    comments = Comment.objects.filter(product=prd).order_by('-date')
    print(comments[0].comment)
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
    context = {}
    return render(request, 'search.html', context)


def items_wanted(request):
    category_ = request.GET["category"]
    search_string = request.GET["search"]
    whichpage = request.GET["page"]
    page_size = request.GET["pageSize"]

    print("category_", category_)

    desired_cat = []
    desired_prod = []

    desired_cat = Category.objects.filter( pk = category_)
    print("desired_cat", desired_cat)

    desired_subcat = SubCats.objects.filter( category = desired_cat[0])
    print("desired_subcat", desired_subcat)

    from itertools import chain
    desired_cats = list(chain(desired_cat, desired_subcat))

    print('desired_cats:', desired_cats)

    if desired_cats:
        for x in desired_cats:
            if Product.objects.filter(category = x):
                desired_prod = list(chain(Product.objects.filter(category = x), desired_prod))

    print('Desired_prod', desired_prod)

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
                if term in elem.name:
                    final_prod.append(elem)
    else:
        final_prod = desired_prod

    print('final_prod',final_prod)


    if not page_size:
        page_size = 8

    paginator = Paginator(final_prod, page_size)

    if not whichpage:
        whichpage = 1

    items = paginator.page(whichpage)
    totalresults = len(final_prod)

    responselist = []
    for elem in final_prod:
        dic_el = {'category': category_, 'price': elem.price, 'id': elem.pk, 'name': elem.name, 'picUrl': elem.image.url }
        responselist.append(dic_el)

    response_data = {"page": whichpage, 'pageSize': len(items), 'totalResults': totalresults, 'productList': responselist}
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def into_search(request, category, search_str):
    context = {'p_category_': category, 'p_search_str_': search_str};
    return render(request, 'search.html', context)


def list_categories(request):
    list_of_cats = Category.objects.all()
    categorylist = []
    for elem in list_of_cats:
        dic_el = {'name': elem.name, 'id': elem.pk}
        categorylist.append(dic_el)

    response_data = {'categoryList': categorylist}
    return HttpResponse(json.dumps(response_data), content_type="application/json")





