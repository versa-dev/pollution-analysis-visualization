from django.urls import path

from . import views

urlpatterns = [
    path('', views.csv_upload, name='upload'),
]