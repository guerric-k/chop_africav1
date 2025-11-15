from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Booking, Review, MenuItem
from django.views.generic import TemplateView
from .forms import BookingForm, ReviewForm

# Create your views here.

class MenuItemListView(ListView):
    model = MenuItem
    template_name = 'menu/menu_list.html'  
    context_object_name = 'menu_items'     
    paginate_by = 6

class HomePageView(TemplateView):
    template_name = 'home.html'

class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'bookings/booking_list.html'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'bookings/booking_form.html'
    success_url = reverse_lazy('booking_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Your reservation was successful.")
        return super().form_valid(form)

class BookingUpdateView(LoginRequiredMixin, UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'bookings/booking_form.html'
    success_url = reverse_lazy('booking_list')

class BookingDeleteView(LoginRequiredMixin, DeleteView):
    model = Booking
    template_name = 'bookings/booking_confirm_delete.html'
    success_url = reverse_lazy('booking_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Reservation successfully deleted.")
        return super().delete(request, *args, **kwargs)

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review_form.html'
    success_url = reverse_lazy('booking_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Thanks for your review!")
        return super().form_valid(form)

class HomePageView(TemplateView):
    template_name = 'home.html'
