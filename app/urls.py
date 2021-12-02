from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('all', views.get_all),
    path('car', views.add_car),
    path('car/<str:car_name>', views.get_car),
]
