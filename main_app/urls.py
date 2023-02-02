from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('flights/', views.flights_index, name='index'),
  path('flights/<int:flight_id>/', views.flights_detail, name='detail'),
  path('flights/create/', views.FlightCreate.as_view(), name='flights_create'),
  path('flights/<int:pk>/update', views.FlightUpdate.as_view(), name='flights_update'),
  path('flights/<int:pk>/delete/', views.FlightDelete.as_view(), name='flights_delete'),
]
