from django.conf.urls import patterns, url

from laptops import views

urlpatterns = patterns('',
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^laptops/(?P<id>[\w\d]+)/$', views.LaptopDetail.as_view(), name='detail'),
	)