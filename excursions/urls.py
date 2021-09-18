from django.urls import path

from . import views

app_name = 'excursions'
urlpatterns = [
    path('', views.ExcursionListView.as_view(), name='list'),
    path('<int:pk>/', views.ExcursionDetailView.as_view(), name='detail'),
    path('<int:pk>/register/', views.RegistrationFormView.as_view(), name='registration'),
    path('<int:pk>/register/success/', views.RegistrationFormDoneView.as_view(), name='registration_done'),
]