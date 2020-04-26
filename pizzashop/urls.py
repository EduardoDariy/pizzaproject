from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^basket_adding/$', views.basket_adding, name='basket_adding'),
    url(r'^item/(?P<item_id>\w+)/$', views.item, name='item'),

]