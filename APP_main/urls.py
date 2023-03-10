from django.urls import path, include
from . import views as vw

urlpatterns = [
    path('', vw.VW_home, name='URL_home'),
    path('about/', vw.VW_about, name='URL_about'),
    path('sponsors/', vw.VW_sponsors, name='URL_sponsors'),
    path('foundation/', vw.VW_foundation, name='VW_foundation'),
    path('contact/', vw.VW_contact, name='URL_contact'),
    path('stats/', vw.VW_stats, name='URL_stats'),
]