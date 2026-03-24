from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Travel Companion!")

# Create your views here.
