# account/urls.py
from django.urls import path, include
from Accounts import views


urlpatterns = [
   
    path('signup/', views.signupuser, name="signupuser"),
    path('login/', views.loginuser, name="loginuser"),
    path('handlelogout/', views.handlelogout, name="handlelogout"),
    

]
