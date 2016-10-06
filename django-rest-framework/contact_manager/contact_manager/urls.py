from django.conf.urls import url
from contact import views

# urlpatterns = [
#     url(r'^contacts/$', views.contact_list),
#     url(r'^contacts/(?P<pk>[0-9]+)$', views.contact_detail),
# ]

urlpatterns = [
    url(r'^contacts/$', views.ContactList.as_view()),
    url(r'^contacts/(?P<pk>[0-9]+)/$', views.ContactDetail.as_view()),
]