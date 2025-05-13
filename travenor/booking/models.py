from django.db import models
from user.models import User
from travel.models import Travels

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    travel = models.ForeignKey(Travels, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    guests_count = models.IntegerField()

    def __str__(self):
        return f"Booking by {self.user} for {self.travel}"

class Payment(models.Model):
    type = [
        ('card', 'card'),
        ('cash', 'cash'),
    ]
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=50)

    def __str__(self):
        return f"Payment for {self.booking}"

