from django.conf.urls import url, patterns
from blog import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^category/(?P<slug>[a-z,0-9,_,-]+)/$', views.category, name='category'),
                       url(r'^(?P<slug>[a-z,0-9,_,-]+)/$', views.post, name='post'),
                       url(r'^search/', views.search, name='search'),
)
