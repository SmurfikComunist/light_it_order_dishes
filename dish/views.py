from django.views import generic
from . import models
from . import forms


class DishIngridientsListView(generic.ListView):
    model = models.DishIngridients
    form_class = forms.DishIngridientsForm


class DishIngridientsCreateView(generic.CreateView):
    model = models.DishIngridients
    form_class = forms.DishIngridientsForm


class DishIngridientsDetailView(generic.DetailView):
    model = models.DishIngridients
    form_class = forms.DishIngridientsForm


class DishIngridientsUpdateView(generic.UpdateView):
    model = models.DishIngridients
    form_class = forms.DishIngridientsForm
    pk_url_kwarg = "pk"


class IngredientListView(generic.ListView):
    model = models.Ingredient
    form_class = forms.IngredientForm


class IngredientCreateView(generic.CreateView):
    model = models.Ingredient
    form_class = forms.IngredientForm


class IngredientDetailView(generic.DetailView):
    model = models.Ingredient
    form_class = forms.IngredientForm


class IngredientUpdateView(generic.UpdateView):
    model = models.Ingredient
    form_class = forms.IngredientForm
    pk_url_kwarg = "pk"


class DishListView(generic.ListView):
    model = models.Dish
    form_class = forms.DishForm


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
    form_class = forms.OrderForm


class OrderCreateView(generic.CreateView):
    model = models.Order
    form_class = forms.OrderForm


class OrderDetailView(generic.DetailView):
    model = models.Order
    form_class = forms.OrderForm


class OrderUpdateView(generic.UpdateView):
    model = models.Order
    form_class = forms.OrderForm
    pk_url_kwarg = "pk"


class OrderIngridientsListView(generic.ListView):
    model = models.OrderIngridients
    form_class = forms.OrderIngridientsForm


class OrderIngridientsCreateView(generic.CreateView):
    model = models.OrderIngridients
    form_class = forms.OrderIngridientsForm


class OrderIngridientsDetailView(generic.DetailView):
    model = models.OrderIngridients
    form_class = forms.OrderIngridientsForm


class OrderIngridientsUpdateView(generic.UpdateView):
    model = models.OrderIngridients
    form_class = forms.OrderIngridientsForm
    pk_url_kwarg = "pk"
