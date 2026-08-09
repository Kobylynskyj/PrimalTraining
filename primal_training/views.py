from django.shortcuts import render, redirect, get_object_or_404
from .models import User, FitnessClass, Reservation
from django.views.generic import TemplateView, ListView,DetailView
from django.views.generic.edit import CreateView
from django.views import View
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


class ReservationCreateView(View):
    def get(self,request,class_id=None):
        fitness_class = get_object_or_404(FitnessClass, id=class_id)
        return render(request, 'reservation_form.html', {'fitness_class': fitness_class})

    def post(self, request, *args, **kwargs):
        class_id = request.POST.get('class_id')
        fitness_class = get_object_or_404(FitnessClass, id=class_id)
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        reser_date= request.POST.get('reser_date')

        user, _  = User.objects.get_or_create(
            email=email,
            defaults={
                'name':name,
                'last_name':last_name,
                'phone':phone,
            }

        )
        Reservation.objects.create(
            user=user,
            fitness_class = fitness_class,
            reser_date=reser_date
        )
        return redirect('HOME')
