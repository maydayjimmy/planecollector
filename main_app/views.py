from django.shortcuts import render
from .models import Flight
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Add the following import
from django.http import HttpResponse

# class Flight:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, airline, number, duration):
#     self.airline = airline
#     self.number = number
#     self.duration = duration

# flights = [
#   Flight('AA', '35', 3.5),
#   Flight('UA', '367', 4),
#   Flight('DL', '445', 2),
# ]

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def flights_index(request):
  flights = Flight.objects.all()
  return render(request, 'flights/index.html', { 'flights': flights })

def flights_detail(request, flight_id):
  flight = Flight.objects.get(id=flight_id)
  return render(request, 'flights/detail.html', { 'flight': flight })

class FlightCreate(CreateView): # class based view
  model = Flight
  fields = ('route', 'airline', 'aircraft', 'number','duration')
  success_url = '/flights/'

class FlightUpdate(UpdateView): # class based view
  model = Flight
  fields = ('route', 'airline', 'aircraft', 'number','duration')
  
class FlightDelete(DeleteView): # class based view
  model = Flight
  success_url= '/flights/'