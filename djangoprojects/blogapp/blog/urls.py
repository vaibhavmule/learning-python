from django.conf.urls import include, url
from django.views.generic import ListView, DetailView
from .models import Post

urlpatterns = [
    url(r'^$', ListView.as_view(
                            queryset=Post.objects.all().order_by('-created')[:2],
                            template_name='blog.html')),
    url(r'^(?P<pk>[1-9]+)/$', DetailView.as_view(
                            model=Post,
                            template_name='post.html')),
]
