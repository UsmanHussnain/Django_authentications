from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from django.db import IntegrityError
from datetime import date, timedelta

# Create your views here.
User = get_user_model()

def home(request):
    return render(request, 'main.html')
@login_required(login_url="/login")
def dashboard(request):
    return render(request, 'base/dashboard.html')
def signup(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        cnic = request.POST.get('cnic')
        dob = request.POST.get('dob')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        
        try:
            user = User.objects.create_user(username=email, email=email, password=password, cnic=cnic, dob=dob, phone=phone, address=address)
            user.save()
            messages.success(request, "Account created successfully")
            return redirect('login')
        except IntegrityError:
            messages.error(request, "That email is already taken.")
    
    today = date.today()
    max_date = today - timedelta(days=10*365 + 3)
    min_date = today - timedelta(days=30*365 + 8)
    
    country_codes = [
        ('+92', 'Pakistan'),
        ('+1', 'United States'),
        ('+44', 'United Kingdom'),
        ('+91', 'India'),
        ('+86', 'China'),
    ]
    
    country_patterns = {
        '+92': r'^\+[0-9]{2}-[0-9]{10}$',  
        '+1': r'^\+[0-9]{1,3}-[0-9]{3}-[0-9]{3}-[0-9]{4}$', 
        '+44': r'^\+[0-9]{2}-[0-9]{4}-[0-9]{4}-[0-9]{4}$',  
        '+91': r'^\+[0-9]{2}-[0-9]{10}$', 
        '+86': r'^\+[0-9]{2}-[0-9]{11}$', 
    }
    
    context = {
        'max_date': max_date.strftime('%Y-%m-%d'),
        'min_date': min_date.strftime('%Y-%m-%d'),
        'country_codes': country_codes,
        'country_patterns': country_patterns,
    }
    
    return render(request, 'base/signup.html', context)

def loginPage(request):
    
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method=="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
    
        try:
            user = User.objects.get(email=email, password=password)
        except:
            messages.error(request, "User does not exsit")

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "email or password incorrect")
            return redirect('login')
    return render(request, 'base/login.html')

@login_required(login_url="/login")
def logoutUser(request):
   
    logout(request)
    return redirect('login')