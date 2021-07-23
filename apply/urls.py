from django.urls import path
from apply.views import *

urlpatterns = [
    path('new/', new, name = 'urlnamenew'),
    path('readall/', readall, name = 'urlnamereadall'),
    path('detail/<str:each_id>', detail, name ='urlnamedetail'),
    path('update/<str:each_id>', update, name= 'urlnameupdate'),
    path('delete/<str:each_id>', delete, name = 'urlnamedelete')
]