from django.shortcuts import render
from django.http import HttpResponse
# This is where you have functions to handle requests and return responses.
# Create your views here.

# You must map this to your urls.py file to get anything to show up.

def index(request):
    return HttpResponse("Hello World")
