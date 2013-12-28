from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Project_Phase2.views.home', name='home'),
    url(r'^$', 'MFSharif.views.index', name = 'index'),
    #url(r'^search', 'MFSharif.views.loadsearch', name = 'search'),
    url(r'^loadproductitems', 'MFSharif.views.items_wanted', name = 'products'),
    url(r'^search/(?P<category>\S+)/(?P<search_str>\S+)', 'MFSharif.views.into_search', name= 'searchintosearchpage'),
    url(r'^categorylisturl', 'MFSharif.views.list_categories', name= 'listing_categories' ),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
