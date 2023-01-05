from django.urls import path, include
from . import views as vw

urlpatterns = [
    path('', vw.VW_news, name='URL_news'),
    path('addnews/', vw.VW_addnews, name='URL_addnews'),
    path('logout/', vw.VW_logout, name='URL_logout'),
]