from .models import Restaurant, Food
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Save', 'Save', css_class='btn-primary'))
    
class FoodForm(forms.ModelForm):
    class Meta:
        model = Food

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Save', 'Save', css_class='btn-primary'))
