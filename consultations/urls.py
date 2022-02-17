from django.urls import path

from . import views

app_name = 'consultations'
urlpatterns = [
    path('', views.ConsultationsView.as_view(), name='main'),
]