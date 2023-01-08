from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView, CreateView
from .models import MO_news
from .forms import FO_addnews, FO_addnews2

# Create your views here.
def VW_news(request):
    all_news = MO_news.objects.all().order_by('-date')
    return render(request, 'news.html', {
        'all_news': all_news
    })

@login_required()
def VW_addnews(request, pk):
    # print('########################################')
    # print(request, pk, pk)
    # print(str(request).find('create'))
    if request.method == 'POST':
        nw_title = request.POST['title']   # Form variable name
        nw_description = request.POST['description']
        nw_image = request.POST['image']

        # selector = 1: CREATE
        # selector != 1: UPDATE
        if pk == 0:
            MO_news.objects.create(
                title = nw_title,
                description = nw_description,
                image = nw_image
            )
        else:
            # MO_news.objects.filter(pk=pk).update(
            MO_news.objects.select_for_update().filter(id=pk).update(
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


def VW_updnews(request, pk):                                         
    data = get_object_or_404(MO_news, id=pk)
    form = FO_addnews2(instance=data)                                                               

    if request.method == "POST":
        form = FO_addnews2(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect ('URL_news')
    context = {
        "form1":form
    }
    return render(request, 'addnews.html', context)


# CREATE
class Create(CreateView):
    template_name = "addnews2.html"
    model = MO_news
    form = FO_addnews2
    fields = '__all__'
    success_url = reverse_lazy('URL_news')

# UPDATE 
class Update(UpdateView):
    model = MO_news
    # form = FO_addnews2
    # context_object_name = 'form1'
    fields = '__all__'
    template_name = "addnews2.html"
    success_url = reverse_lazy('URL_news')

# DELETE 
class Delete(DeleteView):
    model = MO_news
    context_object_name = 'news'
    template_name = "news_confirm_delete.html"
    success_url = reverse_lazy('URL_news')
    # def get_success_url(self):
    #     pass