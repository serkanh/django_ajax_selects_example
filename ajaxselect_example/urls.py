from django.conf.urls import patterns, include, url
from links.views import add_link
from ajax_select import urls as ajax_select_urls
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ajaxselect_example.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/lookups/', include(ajax_select_urls)),
    url(r'^add/$', add_link, name = 'add-link'),
)
