from django.db import models
import uuid
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=30, verbose_name="Ім'я")
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")

    class Meta:
        verbose_name = "Користувач"
        verbose_name_plural = "Користувачі"

        def __str__(self):
            return f"{self.name} - {self.phone}"


class FitnessClass(models.Model):
    title = models.CharField(max_length=100, verbose_name="Назва класу")
    description = models.TextField(verbose_name="Опис")
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, verbose_name="Ціна")
    max_capacity = models.PositiveIntegerField(default=15, verbose_name="Макс. кількість місць")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")

    class Meta:
        verbose_name = "Заняття / Клас"
        verbose_name_plural = "Заняття / Класи"

        def __str__(self):
            return self.title


class Reservation(models.Model):
    STATUS_CHOICES = [
        ('confirmed', 'Підтверджено'),
        ('canceled', 'Скасовано'),
        ('completed', 'Завершено'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations', 
        verbose_name="Користувач")
    fitness_class= models.ForeignKey(FitnessClass, on_delete=models.CASCADE, related_name='reservations', 
        verbose_name="Клас")
    reser_date = models.DateTimeField(verbose_name="Дата та час тренування")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='confirmed', 
        verbose_name="Статус")
    cancel_token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True,
        verbose_name="Токен скасування")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")

    class Meta:
        verbose_name = "Бронювання"
        verbose_name_plural = "Бронювання"
        ordering = ['-created_at']

        def __str__(self):
            return f"{self.user.name} - {self.fitness_class.title} - {self.reser_date.strftime('%Y-%m-%d %H:%M')}"
