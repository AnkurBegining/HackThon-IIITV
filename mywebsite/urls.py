from django.conf.urls import url
from . import views
from mywebsite import views as core_views

urlpatterns = [
    url(r'^$', views.firstPage, name='firstPage'),
]