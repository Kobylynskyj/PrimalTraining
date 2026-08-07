from django.shortcuts import render,redirect
from .models import User, FitnessClass, Reservation
from django.views.generic import TemplateView, ListView,DetailView
from django.views.generic.edit import CreateView
# Create your views here.

class HomePage(TemplateView):
    template_name = 'home_view.html'

class AboutView(TemplateView):
    template_name = 'about_view.html'

class ContactsView(TemplateView):
    template_name = 'contacts_view.html'

class ReserveView(ListView):
    model = FitnessClass
    template_name = 'reserve_view.html'
    context_object_name = 'classes'
    


