from django.shortcuts import render

# Create your views here.
def VW_home(request):
    return render(request, 'home.html')

def VW_about(request):
    return render(request, 'about.html')

def VW_contact(request):
    return render(request, 'contact.html')

def VW_gallery(request):
    return render(request, 'gallery.html')