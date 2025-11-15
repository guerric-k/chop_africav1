from . import views
from django.urls import path
from .views import HomePageView, BookingListView, BookingCreateView, BookingUpdateView, BookingDeleteView, ReviewCreateView, MenuItemListView

app_name = 'bookings'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),              
    path('menu/', MenuItemListView.as_view(), name='menu'),     
    path('bookings/', BookingListView.as_view(), name='booking_list'),
    path('bookings/new/', BookingCreateView.as_view(), name='booking_create'),
    path('bookings/<int:pk>/edit/', BookingUpdateView.as_view(), name='booking_update'),
    path('bookings/<int:pk>/delete/', BookingDeleteView.as_view(), name='booking_delete'),
    path('reviews/new/', ReviewCreateView.as_view(), name='review_create'),
]

