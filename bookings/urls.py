from . import views
from django.urls import path
from .views import HomePageView, MenuItemListView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),              # Root/home page
    path('menu/', MenuItemListView.as_view(), name='menu'),     # Menu page
]