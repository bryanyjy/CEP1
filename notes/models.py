from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=128)
    address = models.TextField()
    food = models.ManyToManyField('Food')
    
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("restaurant_detail", kwargs={"pk":self.pk})

class Food(models.Model):
    name = models.CharField(max_length=128)
    count = models.IntegerField(null=True)
    info = models.TextField(null=True)
    
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("food_detail", kwargs={"pk":self.pk})