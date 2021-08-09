from django import forms
from django.contrib import admin

from . import models


class IngredientAdminForm(forms.ModelForm):

    class Meta:
        model = models.Ingredient
        fields = "__all__"


class IngredientAdmin(admin.ModelAdmin):
    form = IngredientAdminForm
    list_display = [
        "name",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


class DishAdminForm(forms.ModelForm):

    class Meta:
        model = models.Dish
        fields = "__all__"


class DishIngredientsInline(admin.TabularInline):
    model = models.Dish.ingredients.through


class DishAdmin(admin.ModelAdmin):
    form = DishAdminForm
    list_display = [
        "created",
        "name",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]
    inlines = [DishIngredientsInline]


class OrderAdminForm(forms.ModelForm):

    class Meta:
        model = models.Order
        fields = "__all__"


class OrderAdmin(admin.ModelAdmin):
    form = OrderAdminForm
    list_display = [
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


admin.site.register(models.Ingredient, IngredientAdmin)
admin.site.register(models.Dish, DishAdmin)
admin.site.register(models.Order, OrderAdmin)
