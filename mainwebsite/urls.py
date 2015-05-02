from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mainwebsite.views.home', name='home'),
    # url(r'^mainwebsite/', include('mainwebsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','customer.views.home'),
    url(r'^cart$','customer.views.cart',name='cart'),
    url(r'^check_order/(?P<pid>\d+)/(?P<quant>\d+)$','customer.views.check_order',name='check_order'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),


)
