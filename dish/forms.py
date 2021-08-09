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
            "name",
            "ingridients",
        ]


class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = [
            "dish",
            "ingredients",
        ]


