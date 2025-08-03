from django.http import HttpResponse

# Create your views here.
def my_bookings(request):
    return HttpResponse("Hello, Restaurant!")