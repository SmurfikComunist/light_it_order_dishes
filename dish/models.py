from django.db import models
from django.urls import reverse


class DishIngridients(models.Model):

    # Relationships
    dish = models.ForeignKey("dish.Dish", on_delete=models.CASCADE)
    ingredient = models.ForeignKey("dish.Ingredient", on_delete=models.CASCADE)

    # Fields
    ingredients_amount = models.PositiveIntegerField(default=1)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("dish_DishIngridients_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("dish_DishIngridients_update", args=(self.pk,))


class Ingredient(models.Model):

    # Fields
    name = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("dish_Ingredient_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("dish_Ingredient_update", args=(self.pk,))


class Dish(models.Model):

    # Relationships
    ingridients = models.ManyToManyField("dish.Ingredient", through='DishIngridients')

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=255, unique=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("dish_Dish_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("dish_Dish_update", args=(self.pk,))


class Order(models.Model):

    # Relationships
    dish = models.ForeignKey("dish.Dish", on_delete=models.CASCADE)
    ingredients = models.ManyToManyField("dish.Ingredient", through='OrderIngridients')

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("dish_Order_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("dish_Order_update", args=(self.pk,))


class OrderIngridients(models.Model):

    # Relationships
    order = models.ForeignKey("dish.Order", on_delete=models.CASCADE)
    ingridient = models.ForeignKey("dish.Ingredient", on_delete=models.CASCADE)

    # Fields
    ingredients_amount = models.PositiveIntegerField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("dish_OrderIngridients_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("dish_OrderIngridients_update", args=(self.pk,))
