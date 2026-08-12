from django.shortcuts import render, redirect, get_object_or_404
from .models import User, FitnessClass, Reservation
from django.views.generic import TemplateView, ListView,DetailView
from django.views.generic.edit import CreateView
from django.views import View
from django.utils.dateparse import parse_datetime
from  django.db.models import Q
from django.http import JsonResponse
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
        reser_date = parse_datetime(reser_date) if reser_date else None



        existing_user = User.objects.filter(Q(email=email) | Q(phone=phone)).first()

        if existing_user:
            
            if existing_user.email == email and (existing_user.name != name or existing_user.last_name != last_name):
                return JsonResponse({'error': 'A user with this email address already exists.'}, status=400)
            
            
            if existing_user.phone == phone and (existing_user.name != name or existing_user.last_name != last_name):
                return JsonResponse({'error': 'A user with this phone number already exists.'}, status=400)
            

            user = existing_user
        else:
            
            user = User.objects.create(
                name=name,
                last_name=last_name,
                email=email,
                phone=phone
            )

        
        if Reservation.objects.filter(user=user, fitness_class=fitness_class, reser_date=reser_date).exists():
            return JsonResponse({'error': 'You have already created a reservation for this time.'}, status=400)

        
        Reservation.objects.create(
            user=user,
            fitness_class=fitness_class,
            reser_date=reser_date
        )

        return redirect('HOME')
