from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'MFSharif.views.index', name = 'index'),
    url(r'^loadproductitems', 'MFSharif.views.items_wanted', name = 'products'),
    url(r'^search(?:[.]html)?/(?P<category>\w*)(/(?P<search_str>\w*))?', 'MFSharif.views.into_search', name= 'searchintosearchpage'),
    url(r'^categorylisturl', 'MFSharif.views.list_categories', name= 'listing_categories' ),
    url(r'^product/(?P<pro_id>\d+)$', 'MFSharif.views.product_info', name = 'product'),
    url(r'^addComment$', 'MFSharif.views.addComment', name='add_comment'),
    url(r'^addProduct$', 'MFSharif.views.addProduct', name='addProduct'),
    url(r'^addProduct2$', 'MFSharif.views.addProduct2', name='addProduct2'),
    url(r'^upload$', 'MFSharif.views.upload_image', name='upload_image'),
    url(r'^submitProduct', 'MFSharif.views.submit_product', name='submit_product'),
    url(r'^transactions','MFSharif.views.transactions', name = 'transactions'),
    url(r'^editProducts','MFSharif.views.edit_products', name = 'edit-products'),
    url(r'^editP','MFSharif.views.edit_pro', name = 'editp'),
    url(r'^cartProducts','MFSharif.views.cartProducts',name='cartProducts'),
    url(r'^removeCartProduct','MFSharif.views.removeCartProduct',name='removeCartProduct'),
    url(r'^addCartProduct','MFSharif.views.addCartProduct',name='addCartProduct'),
    url(r'^buyProducts','MFSharif.views.buyProducts',name='buyProducts'),
    url(r'^confirmBuy','MFSharif.views.confirmBuy',name='confirmBuy'),
    #url(r'^register/$','MFSharif.views.regFormSent', name='regFormSent'),
    url(r'^doLogin/$', 'MFSharif.views.UserEnter', name= 'UserEnter'),
    url(r'^doLogOut/$', 'MFSharif.views.UserExit', name='UserExit'),
    url(r'Profile$', 'MFSharif.views.ShowProfile', name='ShowProfile'),
    url(r'changeinfo/$', 'MFSharif.views.ChangeInfo', name='ChangeInfo'),



    url(r'^accounts/', include('registration.backends.default.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    ) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)  # for serving media files


if settings.DEBUG:
# static files (images, css, javascript, etc.)
    urlpatterns += patterns('',(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))