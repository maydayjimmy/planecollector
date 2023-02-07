from django.shortcuts import render, redirect
from .models import Flight, Sub
from .forms import HistoryForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# Flights Model ------------------------------------

# page does not display unless logged in
@login_required
def flights_index(request):
  # which flights displayed depends on user that is logged in
  flights = Flight.objects.filter(user=request.user) # user = request.user
  return render(request, 'flights/index.html', { 'flights': flights })

@login_required
def flights_detail(request, flight_id):
  flight = Flight.objects.get(id=flight_id)
  # Get the toys the cat doesn't have
  subs_flight_doesnt_have = Sub.objects.exclude(id__in = flight.subs.all().values_list('id'))
  # instantiate History to be rendered in the template
  history_form = HistoryForm()
  return render(request, 'flights/detail.html', { 
    'flight': flight,
    'history_form': history_form,
    # Add the subs to be displayed
    'subs': subs_flight_doesnt_have
  })
  
# LOGIN REQUIRED MIXIN MUST BE FIRST ARGUMENT ****
class FlightCreate(LoginRequiredMixin, CreateView): # class based view
  model = Flight
  fields = ('route', 'airline', 'aircraft', 'number','duration')
  success_url = '/flights/'

  # This inherited method is called when a
  # valid cat form is being submitted
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)

class FlightUpdate(LoginRequiredMixin, UpdateView): # class based view
  model = Flight
  fields = ('route', 'airline', 'aircraft', 'number','duration')
  
class FlightDelete(LoginRequiredMixin, DeleteView): # class based view
  model = Flight
  success_url= '/flights/'

# -------- History Model ----------------------
@login_required
def add_history(request, flight_id):
  # capture submitted form inputs
  form = HistoryForm(request.POST)
  # validate form inputs
  if form.is_valid():
  # save a temp copy of a new history using the form submission
    new_history = form.save(commit=False)
  # associate the new feeding to the flight using the corresponding flight id
    new_history.flight_id = flight_id
  # save the new history to the database
    new_history.save()
  # return with a response to redirect
  # NOTE: we need to import the built-in redirect function/method
  return redirect('detail', flight_id=flight_id)

@login_required
def assoc_sub(request, flight_id, sub_id):
  # Note that you can pass a subs's id instead of the whole object
  Flight.objects.get(id=flight_id).subs.add(sub_id)
  return redirect('detail', flight_id=flight_id)

# Subs Model ---------- (Class-Based Views)-------------

class SubIndex(LoginRequiredMixin, ListView):
  model = Sub

class SubCreate(LoginRequiredMixin, CreateView):
  model = Sub
  fields = '__all__'
  success_url = '/subs/'

class SubDetail(LoginRequiredMixin, DetailView):
  model = Sub

class SubDelete(LoginRequiredMixin, DeleteView):
  model = Sub
  success_url = '/subs/'

class SubUpdate(LoginRequiredMixin, UpdateView):
  model = Sub
  fields= '__all__'
  success_url = '/subs/'

# ----------------------------- Signup view function -------
def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)