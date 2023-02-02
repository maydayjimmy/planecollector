from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('flights/', views.flights_index, name='index'),
  path('flights/<int:flight_id>/', views.flights_detail, name='detail'),
]
