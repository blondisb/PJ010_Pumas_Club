from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import MO_news

# Create your views here.
def VW_news(request):
    all_news = MO_news.objects.all()
    return render(request, 'news.html', {
        'all_news': all_news
    })

def VW_newdetails(request, pk):
    one_new = get_object_or_404(MO_news, pk=pk)
    return render(request, 'news_details.html',{
        'news':one_new 
    })


@login_required()
def VW_addnews(request):
    return render(request, 'addnews.html')

def VW_logout(request):
    logout(request)
    return redirect('URL_home')