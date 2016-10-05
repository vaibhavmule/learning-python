from django.conf.urls import patterns, url

from laptops import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.LaptopDetail.as_view(), name='detail'),

	)