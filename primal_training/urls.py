from django.urls import path, include
from primal_training.views import HomePage, AboutView,ReserveView,ContactsView, ReservationCreateView




urlpatterns = [
    path('', HomePage.as_view(), name="HOME" ),
    path('about/', AboutView.as_view(), name="ABOUT AS" ),
    path('contacts/', ContactsView.as_view(), name="CONTACTS" ),
    path('reservations/', ReserveView.as_view(), name="RESERVE YOUR SPOT" ),
    
    # URL для обробки POST-запиту з модалки
    path('reserve/create/', ReservationCreateView.as_view(), name='CREATE_RESERVATION'),
]