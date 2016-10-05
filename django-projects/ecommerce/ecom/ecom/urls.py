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
    url(r'^profile/$', 'ecom.views.profile', name='profile'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'ecom.views.home', name='home'),
    url(r'^accounts/', include('registration.backends.default.urls')),
	url(r'^password/change/$',
                auth_views.password_change,
                name='password_change'),
	url(r'^password/change/done/$',
                auth_views.password_change_done,
                name='password_change_done'),
	url(r'^password/reset/$',
                auth_views.password_reset,
                name='password_reset'),
	url(r'^accounts/password/reset/done/$',
                auth_views.password_reset_done,
                name='password_reset_done'),
	url(r'^password/reset/complete/$',
                auth_views.password_reset_complete,
                name='password_reset_complete'),
	url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
                auth_views.password_reset_confirm,
                name='password_reset_confirm'),
)
