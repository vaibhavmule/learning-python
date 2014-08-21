from django.conf.urls import patterns, include, url
from django.conf import settings
from vablog.views import PostListView
from views import PostCreateView, PostDetailView, PostUpdateView, PostDeleteView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', PostListView.as_view(), name='list'),
    url(r'^post/', include(vablog.urls)),
    url(r'^add/$', PostCreateView.as_view(), name='create'),
    url(r'^(?P<pk>[\w\d]+)/$', PostDetailView.as_view(),
    	name='detail'),
    url(r'^(?P<pk>[\w\d]+)/edit/$', PostUpdateView.as_view(),
    	name='update'),
    url(r'^(?P<pk>[\w\d]+)/delete/$', PostDeleteView.as_view(),
    	name='delete')
)
