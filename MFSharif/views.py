from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
import json
from django.http import HttpResponse
from MFSharif.models import *


# Create your views here.
def index(request):
    context = {}
    return render(request, 'base.html', context)


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

    context = {'men_items':men_items, 'women_items': women_items, 'products': pro}
    return render(request, 'base.html', context)


def product_info(request, pro_id):
    pid = int(pro_id)
    pro = Product.objects.filter(pk=pid)
    comments = Comment.objects.filter(product=pro)
    context = {'product':pro, 'comments':comments}
    return render(request,'ProductDetail.html', context)


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

    if desired_cat:
        for x in desired_cat:
            desired_prod = Product.objects.filter(category = x)

    if search_string:
        qset = Q()
        for term in search_string.split():
            qset |= Q(name__contains = term)
        desired_prod = desired_prod.filter(qset)

    if not page_size:
        page_size = 8

    paginator = Paginator(desired_prod, page_size)

    if not whichpage:
        whichpage = 1

    items = paginator.page(whichpage)
    totalresults = len(desired_prod)

    responselist = []
    for elem in desired_prod:
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





