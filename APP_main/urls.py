from django.urls import path, include
from . import views as vw

urlpatterns = [
    path('', vw.VW_home, name='URL_home')
]