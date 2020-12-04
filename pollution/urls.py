from django.urls import path


from . import views

urlpatterns = [
	path('pollution', views.pollution_table, name='pollution'),
    path('vehicles', views.vehicle_table, name='vehicle'),
    path('cities', views.city_table, name='city'),
]