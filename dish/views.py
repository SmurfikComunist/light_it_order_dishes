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


class BaseDishOrderCreateUpdateView(generic.UpdateView):
    pk_url_kwarg = "pk"
    context_formset = None
    formset_type = None

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except AttributeError:
            return None

    def get_initial_data(self):
        return None

    def form_valid(self, form):
        context = self.get_context_data(form=form)
        formset = context[self.context_formset]

        if formset.is_valid():
            response = super().form_valid(form)

            formset.instance = self.object
            formset.save()

            return response
        else:
            return super().form_invalid(form)


class BaseDishCreateUpdateView(BaseDishOrderCreateUpdateView):
    model = models.Dish
    form_class = forms.DishForm
    context_formset = "dish_ingredients_formset"
    formset_type = forms.DishIngredientsFormset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        formset = None

        initial_data = self.get_initial_data()

        if self.request.method == "GET":
            formset = self.formset_type(instance=initial_data)
        elif self.request.method == "POST":
            formset = self.formset_type(self.request.POST, instance=initial_data)

        context[self.context_formset] = formset

        return context


class DishCreateView(BaseDishCreateUpdateView):
    pass


class DishUpdateView(BaseDishCreateUpdateView):
    def get_initial_data(self):
        pk = self.kwargs.get(self.pk_url_kwarg)

        queryset = models.Dish.objects.prefetch_related(
            'dish_ingredients__ingredient'
        ).filter(pk=pk)

        return queryset.get()


class DishDetailView(generic.DetailView):
    model = models.Dish

    def get_queryset(self):
        return models.Dish.objects.prefetch_related(
            'dish_ingredients__ingredient'
        )


class OrderListView(generic.ListView):
    model = models.Order

    def get_queryset(self):
        return models.Order.objects.select_related(
            'dish'
        )


class BaseOrderCreateUpdateView(BaseDishOrderCreateUpdateView):
    model = models.Order
    form_class = forms.OrderForm
    context_formset = "order_ingredients_formset"
    formset_type = forms.OrderIngredientsFormset


class OrderCreateView(BaseOrderCreateUpdateView):
    dish_id_kwarg = "dish_id"

    def get_initial_data(self):
        pk = self.kwargs.get(self.dish_id_kwarg)

        ingredients = models.DishIngredients.objects.\
            select_related("ingredient").\
            filter(dish__id=pk).\
            values("ingredient", "ingredient__name", "ingredients_amount")\
            .all()

        return ingredients

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        formset = None

        if self.request.method == "GET":
            pk = self.kwargs.get(self.dish_id_kwarg)

            dish = models.Dish.objects.filter(pk=pk)

            initial_data = self.get_initial_data()

            formset = self.formset_type(initial=initial_data)
            formset.extra = len(initial_data)

            context['form'].fields['dish'].queryset = dish
            context['form'].fields['dish'].empty_label = None
        elif self.request.method == "POST":
            formset = self.formset_type(self.request.POST)

        context[self.context_formset] = formset

        return context


class OrderDetailView(generic.DetailView):
    model = models.Order

    def get_queryset(self):
        return models.Order.objects.prefetch_related(
            'order_ingredients__ingredient'
        )
