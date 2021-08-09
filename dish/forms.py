from django import forms
from . import models




class IngredientForm(forms.ModelForm):
    class Meta:
        model = models.Ingredient
        fields = [
            "name",
        ]


class DishForm(forms.ModelForm):
    class Meta:
        model = models.Dish
        fields = [
            "name"
        ]


class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = [
            "dish"
        ]


