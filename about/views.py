from django.views.generic.detail import DetailView
from .models import About

class AboutPageView(DetailView):
    model = About
    template_name = 'about/about.html'
    context_object_name = 'about'

    def get_object(self):
        return About.objects.last()  # Use latest About instance
