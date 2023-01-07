from django.urls import path, include
from . import views as vw
# from django.conf.urls.static import static
# from PJ_Pumas.settings import MEDIA_ROOT2, MEDIA_URL2


urlpatterns = [
    path('', vw.VW_news, name='URL_news'),
    path('newdetails/<int:pk>/', vw.VW_newdetails, name='URL_new_details'),
    path('addnews/', vw.VW_addnews, name='URL_addnews'),
    path('update/<int:pk>/', vw.Update.as_view(), name='URL_updnews'),
    path('delete/<int:pk>/', vw.Delete.as_view(), name='URL_delnews'),
    path('logout/', vw.VW_logout, name='URL_logout'),
]

# urlpatterns += static(MEDIA_URL2, document_root=MEDIA_ROOT2)
