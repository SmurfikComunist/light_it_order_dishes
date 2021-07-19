from django.urls import path

from . import views

urlpatterns = (
    path("dish/DishIngridients/", views.DishIngridientsListView.as_view(), name="dish_DishIngridients_list"),
    path("dish/DishIngridients/create/", views.DishIngridientsCreateView.as_view(), name="dish_DishIngridients_create"),
    path("dish/DishIngridients/detail/<int:pk>/", views.DishIngridientsDetailView.as_view(), name="dish_DishIngridients_detail"),
    path("dish/DishIngridients/update/<int:pk>/", views.DishIngridientsUpdateView.as_view(), name="dish_DishIngridients_update"),

    path("dish/Ingredient/", views.IngredientListView.as_view(), name="dish_Ingredient_list"),
    path("dish/Ingredient/create/", views.IngredientCreateView.as_view(), name="dish_Ingredient_create"),
    path("dish/Ingredient/detail/<int:pk>/", views.IngredientDetailView.as_view(), name="dish_Ingredient_detail"),
    path("dish/Ingredient/update/<int:pk>/", views.IngredientUpdateView.as_view(), name="dish_Ingredient_update"),

    path("dish/Dish/", views.DishListView.as_view(), name="dish_Dish_list"),
    path("dish/Dish/create/", views.DishCreateView.as_view(), name="dish_Dish_create"),
    path("dish/Dish/detail/<int:pk>/", views.DishDetailView.as_view(), name="dish_Dish_detail"),
    path("dish/Dish/update/<int:pk>/", views.DishUpdateView.as_view(), name="dish_Dish_update"),

    path("dish/Order/", views.OrderListView.as_view(), name="dish_Order_list"),
    path("dish/Order/create/", views.OrderCreateView.as_view(), name="dish_Order_create"),
    path("dish/Order/detail/<int:pk>/", views.OrderDetailView.as_view(), name="dish_Order_detail"),
    path("dish/Order/update/<int:pk>/", views.OrderUpdateView.as_view(), name="dish_Order_update"),

    path("dish/OrderIngridients/", views.OrderIngridientsListView.as_view(), name="dish_OrderIngridients_list"),
    path("dish/OrderIngridients/create/", views.OrderIngridientsCreateView.as_view(), name="dish_OrderIngridients_create"),
    path("dish/OrderIngridients/detail/<int:pk>/", views.OrderIngridientsDetailView.as_view(), name="dish_OrderIngridients_detail"),
    path("dish/OrderIngridients/update/<int:pk>/", views.OrderIngridientsUpdateView.as_view(), name="dish_OrderIngridients_update"),
)
