from django.urls import path

from . import views

app_name = 'about'
urlpatterns = [
    path('upload/', views.upload_file, name='upload-form'),
]
