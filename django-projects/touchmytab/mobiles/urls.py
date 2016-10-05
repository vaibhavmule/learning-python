from django.conf.urls import patterns, url

from mobiles import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<slug>[-_\w]+)/$', views.MobileDetail.as_view(), name='detail'),

	)