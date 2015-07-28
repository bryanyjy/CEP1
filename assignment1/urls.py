from django.conf.urls import patterns, include, url
from django.contrib import admin
from notes import views
from notes.models import Restaurant, Food
from django.views.generic import DetailView

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^restaurants/$', views.RestaurantList.as_view(template_name="notes/restaurants.html", context_object_name="restaurant_list"), name='restaurant_list'),
    url(r'^restaurants/add/$', views.RestaurantCreate.as_view(), name='restaurant_add'),
    url(r'^restaurants/(?P<pk>\d+)$', DetailView.as_view(model=Restaurant, template_name='notes/restaurant.html'), name='restaurant_detail'),
    url(r'^restaurants/(?P<pk>\d+)/edit/$', views.RestaurantUpdate.as_view(),  name='restaurant_update'),
    url(r'^restaurants/(?P<pk>\d+)/delete/$', views.RestaurantDelete.as_view(),  name='restaurant_delete'),
    url(r'^food/$', views.FoodList.as_view(template_name="notes/allfood.html", context_object_name="food_list"), name='food_list'),
    url(r'^food/(?P<pk>\d+)$', DetailView.as_view(model=Food, template_name="notes/food.html"), name='food_detail'),
    url(r'^food/(?P<pk>\d+)/edit/$', views.FoodUpdate.as_view(),  name='food_update'),
    url(r'^admin/', include(admin.site.urls)),
)
