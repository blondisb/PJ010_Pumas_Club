from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def VW_home(request):
    return render(request, 'home.html')

def VW_about(request):
    return render(request, 'about.html')

def VW_contact(request):
    return render(request, 'contact.html')