from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse


class DishIngredients(models.Model):

    # Relationships
    dish = models.ForeignKey("dish.Dish", on_delete=models.CASCADE)
    ingredient = models.ForeignKey("dish.Ingredient", on_delete=models.CASCADE)

    # Fields
    ingredients_amount = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1)]
    )

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("dish_DishIngredients_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("dish_DishIngredients_update", args=(self.pk,))


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
    ingredients = models.ManyToManyField("dish.Ingredient", through='DishIngredients')

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
    ingredients = models.ManyToManyField("dish.Ingredient", through='OrderIngredients')

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


class OrderIngredients(models.Model):

    # Relationships
    order = models.ForeignKey(
        "dish.Order",
        on_delete=models.CASCADE,
        related_name="order_ingredients")
    ingredient = models.ForeignKey("dish.Ingredient", on_delete=models.CASCADE)

    # Fields
    ingredients_amount = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1)]
    )

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("dish_OrderIngredients_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("dish_OrderIngredients_update", args=(self.pk,))
