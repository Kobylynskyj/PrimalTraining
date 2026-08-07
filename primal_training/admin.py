from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import User, FitnessClass, Reservation

# Register your models here.

@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email', 'phone')


@admin.register(FitnessClass)
class FintnessClassAdmin(ModelAdmin):
    list_display = ('title', 'description','price', 'max_capacity', 'created_at')
    search_fields = ('title',)


@admin.register(Reservation)
class ReservationAdmin(ModelAdmin):
    list_display = ('user', 'fitness_class', 'reser_date', 'status', 'created_at')
    list_filter = ('status', 'fitness_class', 'reser_date')
    search_fields = ('user__name', 'user__phone', 'fitness_class__title')
    readonly_fields = ('cancel_token', 'created_at')

