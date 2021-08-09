from django.views import generic

from . import forms
from . import models


class IngredientListView(generic.ListView):
    model = models.Ingredient
    form_class = forms.IngredientForm


class IngredientCreateView(generic.CreateView):
    model = models.Ingredient
    form_class = forms.IngredientForm


class IngredientDetailView(generic.DetailView):
    model = models.Ingredient


class IngredientUpdateView(generic.UpdateView):
    model = models.Ingredient
    form_class = forms.IngredientForm
    pk_url_kwarg = "pk"


class DishListView(generic.ListView):
    model = models.Dish


class DishCreateView(generic.CreateView):
    model = models.Dish
    form_class = forms.DishForm


class DishDetailView(generic.DetailView):
    model = models.Dish
    form_class = forms.DishForm


class DishUpdateView(generic.UpdateView):
    model = models.Dish
    form_class = forms.DishForm
    pk_url_kwarg = "pk"


class OrderListView(generic.ListView):
    model = models.Order


class OrderCreateView(generic.CreateView):
    model = models.Order
    form_class = forms.OrderForm


class OrderDetailView(generic.DetailView):
    model = models.Order


class OrderUpdateView(generic.UpdateView):
    model = models.Order
    form_class = forms.OrderForm
    pk_url_kwarg = "pk"








