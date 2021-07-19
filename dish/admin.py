from django.contrib import admin
from django import forms

from . import models


class DishIngridientsAdminForm(forms.ModelForm):

    class Meta:
        model = models.DishIngridients
        fields = "__all__"


class DishIngridientsAdmin(admin.ModelAdmin):
    form = DishIngridientsAdminForm
    list_display = [
        "ingredients_amount",
    ]
    readonly_fields = [
        "ingredients_amount",
    ]


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
        "name",
        "created",
        "last_updated",
    ]


class DishAdminForm(forms.ModelForm):

    class Meta:
        model = models.Dish
        fields = "__all__"


class DishAdmin(admin.ModelAdmin):
    form = DishAdminForm
    list_display = [
        "created",
        "name",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "name",
        "last_updated",
    ]


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


class OrderIngridientsAdminForm(forms.ModelForm):

    class Meta:
        model = models.OrderIngridients
        fields = "__all__"


class OrderIngridientsAdmin(admin.ModelAdmin):
    form = OrderIngridientsAdminForm
    list_display = [
        "ingredients_amount",
    ]
    readonly_fields = [
        "ingredients_amount",
    ]


admin.site.register(models.DishIngridients, DishIngridientsAdmin)
admin.site.register(models.Ingredient, IngredientAdmin)
admin.site.register(models.Dish, DishAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.OrderIngridients, OrderIngridientsAdmin)
