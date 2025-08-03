from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# Create your models here.

# Model for restaurant tables
class Table(models.Model):
    LOCATION_CHOICES = [
        ('indoor', 'Indoor'),
        ('outdoor', 'Outdoor'),
    ]
    number = models.PositiveIntegerField(unique=True)
    location = models.CharField(max_length=10, choices=LOCATION_CHOICES)
    wheelchair_accessible = models.BooleanField(default=False)

    def __str__(self):
        return f"Table {self.number} ({self.location})"

# Model for bookings

# Status choices for bookings
STATUS = ((0, 'Pending'), (1, 'Confirmed'), (2, 'Cancelled'))

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    children = models.PositiveIntegerField(default=0)
    special_needs = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        unique_together = ('user', 'date')
    
    def clean(self):
        super().clean()
        if Booking.objects.filter(date=self.date).count() >= 12:
            raise ValidationError("Sorry! There are no available slots for this day. please check another date.")

    def __str__(self):
        return f"{self.user} - {self.date} @ {self.time} status {self.status}"

