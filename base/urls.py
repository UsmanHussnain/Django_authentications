from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginPage, name='login'),
    path('logoutUser/', views.logoutUser, name='logoutUser'),
    path('send_email/', views.send_email, name='send_email'),
    path('verify/<str:token>/', views.verify_email, name='verify_email'),
    path('create-blog', views.create_blogs, name = 'create-blog'),
    
    
   
]