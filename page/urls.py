from django.conf.urls import url
from page import views


urlpatterns = [
    url(r'^(?P<slug>[a-z,0-9,_,-]+)/?$', views.page, name='page'),
]
