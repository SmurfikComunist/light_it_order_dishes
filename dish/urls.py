from django.urls import path

from . import views

urlpatterns = (
    path("ingredients/", views.IngredientListView.as_view(), name="ingredient_list"),
    path("ingredient/create/", views.IngredientCreateView.as_view(), name="ingredient_create"),
    path("ingredient/detail/<int:pk>/", views.IngredientDetailView.as_view(), name="ingredient_detail"),
    path("ingredient/update/<int:pk>/", views.IngredientUpdateView.as_view(), name="ingredient_update"),

    path("dishes/", views.DishListView.as_view(), name="dish_list"),
    path("dish/create/", views.DishCreateView.as_view(), name="dish_create"),
    path("dish/detail/<int:pk>/", views.DishDetailView.as_view(), name="dish_detail"),
    path("dish/update/<int:pk>/", views.DishUpdateView.as_view(), name="dish_update"),

    path("orders/", views.OrderListView.as_view(), name="order_list"),
    path("order/create/<int:dish_id>/", views.OrderCreateView.as_view(), name="order_create"),
    path("order/detail/<int:pk>/", views.OrderDetailView.as_view(), name="order_detail"),
)
