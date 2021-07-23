from django.urls import path
from account.views import *

urlpatterns = [
    path('login/', login_view, name = 'urlnamelogin'),
    path('signup/', signup_view, name = 'urlnamesignup'),
    path('logout/', logout_view, name = 'urlnamelogout'),
    
]