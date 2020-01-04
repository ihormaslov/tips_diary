from django.conf.urls import url
from blog import views


urlpatterns = [
   url(r'^$', views.index, name='index'),
   url(r'^ads\.txt$', views.ads_txt, name='ads_txt'),
   url(r'^category/(?P<slug>[a-z,0-9,_,-]+)/$', views.category, name='category'),
   url(r'^(?P<slug>[a-z,0-9,_,-]+)/$', views.post, name='post'),
   url(r'^search/', views.search, name='search'),
]
