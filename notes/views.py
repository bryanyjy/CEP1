from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse, reverse_lazy
from .models import Restaurant, Food
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import RestaurantForm, FoodForm

# Create your views here.
def home(request):
    return render(request, 'notes/home.html')

class RestaurantList(ListView):
    model = Restaurant
    def get_queryset(self):
        return Restaurant.objects.all().order_by("name")
        
class RestaurantCreate(CreateView):
    model = Restaurant
    form_class = RestaurantForm
    
class RestaurantUpdate(UpdateView):
    model = Restaurant
    form_class = RestaurantForm

class RestaurantDelete(DeleteView):
    model = Restaurant
    success_url = reverse_lazy('listall')

class FoodList(ListView):
    model = Food
    def get_queryset(self):
        return Food.objects.all()
        
class FoodUpdate(UpdateView):
    model = Food
    form_class = FoodForm