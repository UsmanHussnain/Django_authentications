from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginPage, name='login'),
    path('logoutUser/', views.logoutUser, name='logoutUser'),
   
]

