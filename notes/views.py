from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from .models import Restaurant, Food

# Create your views here.
def home(request):
    return render(request, 'notes/home.html')
    
def restaurants_list(request):
    allr = Restaurant.objects.all().order_by("name")
    return render(request, 'notes/restaurants.html', {'restaurants': allr})
    
def restaurant(request, r_id):
    restaurant = Restaurant.objects.get(id=r_id)
    food = Food.objects.all()
    
    return render(request, 'notes/restaurant.html', {'restaurant':restaurant, 'food':food})

def food_list(request):
    allf = Food.objects.all().order_by("name")
    return render(request, 'notes/allfood.html', {'food': allf})
    
def food(request, f_id):
    food = Food.objects.get(id=f_id)
    return render(request, 'notes/food.html', {'food': food})