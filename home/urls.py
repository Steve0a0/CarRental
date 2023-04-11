from django.urls import path
from . import views
from home.APIS.rating import RatingAPI 
urlpatterns = [
    path("", views.index, name="index"),
    path("customer_signup/", views.customer_signup, name="customer_signup"),
    path("customer_login/", views.customer_login, name="customer_login"),
    path("car_dealer_signup/", views.car_dealer_signup, name="car_dealer_signup"),
    path("car_dealer_login/", views.car_dealer_login, name="car_dealer_login"),
    path("add_car/", views.add_car, name="add_car"),
    path("all_cars/", views.all_cars, name="all_cars"),
    path("edit_car/<int:myid>/", views.edit_car, name="edit_car"),
    path("delete_car/<int:myid>/", views.delete_car, name="delete_car"),
    path("customer_homepage/", views.customer_homepage, name="customer_homepage"),
    path("search_results/", views.search_results, name="search_results"),
    path("car_rent/", views.car_rent, name="car_rent"),
    path("order_details/", views.order_details, name="order_details"),
    path("past_orders/", views.past_orders, name="past_orders"),
    path("delete_order/<int:myid>/", views.delete_order, name="delete_order"),
    path("all_orders/", views.all_orders, name="all_orders"),
    path("complete_order/", views.complete_order, name="complete_order"),
    path("earnings/", views.earnings, name="earnings"),
    path("signout/", views.signout, name="signout") ,
     path('map_api/', views.map_api, name='map_api'),

    path("rate_car/<int:pk>/" , views.rate_car , name="rate_car"),

    # API VIEWS
   # path("rating-data-api/", rating_data_api, name="rating-data-api"),
    path("rating-api/", RatingAPI.as_view(), name="rating-api" ),
    
]