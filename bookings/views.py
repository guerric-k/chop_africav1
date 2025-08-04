from django.shortcuts import render
from django.views.generic import ListView
from .models import MenuItem

# Create your views here.

class MenuItemListView(ListView):
    model = MenuItem
    template_name = 'menu/menu_list.html'  
    context_object_name = 'menu_items'     
    paginate_by = 6