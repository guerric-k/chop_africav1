from django.contrib import admin
from .models import Table, Booking, MenuItem, Review

# Register your models here.
admin.site.register(Table)
admin.site.register(Booking)
admin.site.register(MenuItem)
admin.site.register(Review)