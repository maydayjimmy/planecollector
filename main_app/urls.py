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
  path('flights/<int:flight_id>/add_history/', views.add_history, name='add_history'),
      # associate aircrafts with flights (M:M)
  path('flights/<int:flight_id>/assoc_sub/<int:sub_id>/', views.assoc_sub, name='assoc_sub'),
  path('subs/', views.SubIndex.as_view(), name='sub_index'),
  path('subs/<int:pk>/', views.SubDetail.as_view(), name='sub_detail'),
  path('subs/create/', views.SubCreate.as_view(), name='sub_create'),
  path('subs/<int:pk>/update', views.SubUpdate.as_view(), name='sub_update'),
  path('subs/<int:pk>/delete/', views.SubDelete.as_view(), name='sub_delete'),
  path('accounts/signup/', views.signup, name='signup'),
]
