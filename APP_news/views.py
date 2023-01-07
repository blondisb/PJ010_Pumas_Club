from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView
from .models import MO_news
from .forms import FO_addnews

# Create your views here.
def VW_news(request):
    all_news = MO_news.objects.all().order_by('-date')
    return render(request, 'news.html', {
        'all_news': all_news
    })

@login_required()
def VW_addnews(request):
    if request.method == 'POST':
        nw_title = request.POST['title']   # Form variable name
        nw_description = request.POST['description']
        nw_image = request.POST['image']
        # print("#########################################")
        # print(nw_image)

        MO_news.objects.create(
            title = nw_title,
            description = nw_description,
            image = nw_image
        )
        return redirect('URL_news')
    
    elif request.method == 'GET':
        return render(request, 'addnews.html', {
            'form1' : FO_addnews()
        })

def VW_logout(request):
    logout(request)
    return redirect('URL_home')



def VW_newdetails(request, pk):
    one_new = get_object_or_404(MO_news, pk=pk)
    return render(request, 'news_details.html',{
        'news':one_new 
    })


# UPDATE 
class Update(UpdateView):
    model = MO_news
    fields = '__all__'
    template_name = "addnews2.html"
    success_url = reverse_lazy('URL_news')

# DELETE 
class Delete(DeleteView):
    model = MO_news
    context_object_name = 'news'
    template_name = "news_confirm_delete.html"
    success_url = reverse_lazy('URL_news')