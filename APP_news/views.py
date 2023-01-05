from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def VW_news(request):
    return render(request, 'news.html')

@login_required()
def VW_addnews(request):
    return render(request, 'addnews.html')

def VW_logout(request):
    logout(request)
    return redirect('URL_home')