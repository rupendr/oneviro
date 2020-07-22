from django.shortcuts import render, redirect
from .models import AboutTeam


def home(request):
    return render(request, 'home.html')


def about_us(request):
    team_data = AboutTeam.objects.all()
    return render(request, 'about-us.html', {'team_data': team_data})


def services(request):
    return render(request, 'services.html')


def career(request):
    return render(request, 'career.html')


def contact(request):
    return render(request, 'contact.html')
