from django.contrib import admin
from .models import Table, Booking, MenuItem, Review
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
admin.site.register(Table)
admin.site.register(MenuItem)
admin.site.register(Booking)
admin.site.register(Review, SummernoteModelAdmin) 
