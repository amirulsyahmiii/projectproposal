from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return HttpResponse("Hello! This is a django project from Thundering Jaguars using Ubuntu!")

def welcome(request):
	return render(request, 'welcome.html')

# Create your views here
