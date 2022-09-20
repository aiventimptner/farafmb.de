from django.urls import path

from . import views

app_name = 'merchandise'
urlpatterns = [
    path('', views.OrderCreate.as_view(), name='order_create'),
]
