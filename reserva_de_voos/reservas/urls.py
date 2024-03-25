from django.urls import path
from .views import index, main_login, main_page2, login_adm, adm_voo, cad_user, cad_voo, list_voo

urlpatterns =[
    
    path('', index, name='index'),
    path('login/', main_login, name='main_login'),
    path('main/', main_page2, name='main_page2'),
    path('loginadm/', login_adm, name='login_adm'),
    path('caduser/', cad_user, name='cad_user'),
    path('admvoo/', adm_voo, name='adm_voo'),
    path('cadvoo/', cad_voo, name='cad_voo'),
    path('listvoo/', list_voo, name='list_voo')

    
]