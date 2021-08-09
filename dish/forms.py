from django import forms
from django.forms import inlineformset_factory

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


DishIngredientsFormset = inlineformset_factory(
    parent_model=models.Dish,
    model=models.DishIngredients,
    fields=["ingredient", "ingredients_amount"],
    labels={
        "ingredient": "Ingredient name",
        "amount": "Ingredient amount"
    },
    extra=models.Ingredient.objects.count(),
    can_delete=False
)


class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = [
            "dish"
        ]


OrderIngredientsFormset = inlineformset_factory(
    parent_model=models.Order,
    model=models.OrderIngredients,
    fields=["ingredient", "ingredients_amount"],
    labels={
        "ingredient": "Ingredient name",
        "amount": "Ingredient amount"
    },
    can_delete=False
)
