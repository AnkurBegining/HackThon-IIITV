from django.conf.urls import url
from . import views
from mywebsite import views as core_views

urlpatterns = [
    url(r'^$', views.firstPage, name='firstPage'),
    url(r'^secondpage/$', views.post_list, name='post_list'),
    url(r'^secondpage/post/new/$', views.post_new, name='post_new'),
    url(r'^secondpage/post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^secondpage/post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),

]