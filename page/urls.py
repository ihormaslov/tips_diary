from django.conf.urls import url, patterns
from page import views


urlpatterns = patterns('',
                       url(r'^(?P<slug>[a-z,0-9,_,-]+)/?$', views.page, name='page'),
)
