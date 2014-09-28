from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin

from views import home, profile

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ecom.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^laptops/', include('laptops.urls', namespace="laptops")),
    url(r'^mobiles/', include('mobiles.urls', namespace="mobiles")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'ecom.views.home', name='home'),
)
