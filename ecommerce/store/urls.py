from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('product/<int:pk>/', views.Details.as_view(), name="details"),
    path('checkout/', views.checkout, name="checkout"),
]
