from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to My Django Blog!</h1><p>Setup complete. Start building!</p>")