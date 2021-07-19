from django import forms
from . import models


class DishIngridientsForm(forms.ModelForm):
    class Meta:
        model = models.DishIngridients
        fields = [
            "ingredients_amount",
            "dish",
            "ingredient",
        ]


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


class OrderIngridientsForm(forms.ModelForm):
    class Meta:
        model = models.OrderIngridients
        fields = [
            "ingredients_amount",
            "order",
            "ingridient",
        ]
