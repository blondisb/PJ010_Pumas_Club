from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import datetime

# Create your views here.
def VW_home(request):
    return render(request, 'home.html')

def VW_stats(request):
    return render(request, 'stats.html')

def VW_about(request):
    return render(request, 'about.html')

def VW_sponsors(request):
    return render(request, 'sponsors.html')

def VW_foundation(request):
    return render(request, 'foundation.html')

def VW_contact(request):
    return render(request, 'contact.html')