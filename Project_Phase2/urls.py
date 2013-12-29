from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings

admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Project_Phase2.views.home', name='home'),
    url(r'^$', 'MFSharif.views.index', name = 'index'),
    #url(r'^search', 'MFSharif.views.loadsearch', name = 'search'),
    url(r'^loadproductitems', 'MFSharif.views.items_wanted', name = 'products'),
    url(r'^search(?:[.]html)?/(?P<category>\S*)(/(?P<search_str>\S*))?', 'MFSharif.views.into_search', name= 'searchintosearchpage'),
    url(r'^categorylisturl', 'MFSharif.views.list_categories', name= 'listing_categories' ),
    url(r'^product/(?P<pro_id>\d+)$', 'MFSharif.views.product_info', name = 'product'),
    url(r'^addComment$', 'MFSharif.views.addComment', name='add_comment'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
# static files (images, css, javascript, etc.)
    urlpatterns += patterns('',(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))