from django.conf.urls import url
from . import views
from mywebsite import views as core_views

urlpatterns = [
    url(r'^$', views.firstPage, name='firstPage'),
    url(r'^accounts/signup/$', core_views.signup, name='signup'),
    url(r'^tedx/$', core_views.tedx, name='tedx'),
    url(r'^selfmade/$', core_views.selfmade, name='selfmade'),
    url(r'^motivational/$', core_views.motivational, name='motivational'),
    url(r'^institutional/$', core_views.institutional, name='institutional'),
    url(r'^government-initiatives/$', core_views.Government_Initiatives, name='Government_Initiatives'),
    url(r'^digital-marketing/$', core_views.DigitalMarketing, name='DigitalMarketing'),
    url(r'^blog/$', core_views.blog, name='blog'),
    url(r'^create-blog/$', core_views.createblog, name='createblog'),
    url(r'^create-workshop/$', views.CreateWorkshop, name='createworkshop'),
    url(r'^videos/$', views.videos, name='videos'),
    url(r'^workshop/$',views.workshop, name='workshop'),
    url(r'^secondpage/$', views.post_list, name='post_list'),
    url(r'^secondpage/post/new/$', views.post_new, name='post_new'),
    url(r'^secondpage/post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^secondpage/post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^secondpage/post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^secondpage/comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^secondpage/comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),

]