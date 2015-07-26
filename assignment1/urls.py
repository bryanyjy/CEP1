from django.conf.urls import patterns, include, url
from django.contrib import admin
from notes import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^restaurants/$', views.restaurants_list, name='restaurants_list'),
    url(r'^restaurants/(?P<r_id>\d+)$', views.restaurant, name='detail'),
    url(r'^food/$', views.food_list, name='food_list'),
    url(r'^food/(?P<f_id>\d+)$', views.food, name='detail'),
    url(r'^admin/', include(admin.site.urls)),
)
