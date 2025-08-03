from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.PositiveIntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user}"

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
        return f"Booking for {self.user} - {self.date} at {self.time} |status: {self.get_status_display()}"

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user}"