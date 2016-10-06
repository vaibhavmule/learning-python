# from django.conf.urls import url
# from contact import views

# urlpatterns = [
#     url(r'^contacts/$', views.contact_list),
#     url(r'^contacts/(?P<pk>[0-9]+)$', views.contact_detail),
# ]

# urlpatterns = [
#     url(r'^contacts/$', views.ContactList.as_view()),
#     url(r'^contacts/(?P<pk>[0-9]+)/$', views.ContactDetail.as_view()),
# ]

from django.conf.urls import url, include
from contact import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'contacts', views.ContactViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]