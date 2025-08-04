from . import views
from django.urls import path

urlpatterns = [
    path('', views.MenuItemListView.as_view(), name='menu'),
]