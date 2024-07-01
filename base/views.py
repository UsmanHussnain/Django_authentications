from django.shortcuts import render, redirect , get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login , logout , get_user_model
from django.contrib import messages
from django.db import IntegrityError
from datetime import date, timedelta
from django.urls import reverse
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.conf import settings

# Create your views here.
User = get_user_model()


def send_email(request):    
    return redirect('login')


def home(request):
    return render(request, 'main.html')
@login_required(login_url="/login")
def dashboard(request):
    return render(request, 'base/dashboard.html')

def verify_email(request, token):
    user = get_object_or_404(User, verification_token=token)

    if not user.is_verified:
        user.is_verified = True
        user.save()
        messages.success(request, 'Your email has been verified successfully. You can now log in.')
    else:
        messages.info(request, 'Your email is already verified.')

    return redirect('login')
       
def signup(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        cnic = request.POST.get('cnic')
        dob = request.POST.get('dob')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        
        try:
            token = get_random_string(length=32)
            user = User.objects.create_user(username=email, email=email, password=password, cnic=cnic, dob=dob, phone=phone, address=address,verification_token = token)
            
            verification_url = request.build_absolute_uri(reverse('verify_email', kwargs={'token': token}))
            send_mail(
                'Verify your email address',
                f'Click the link to verify your email: {verification_url}',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            messages.success(request, "Account created successfully, Please check your email for verification")
            return redirect('login')
        except IntegrityError as e:
            if 'UNIQUE constraint' in str(e):
                messages.error(request, "That email is already taken.")
            else:
                e
    
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
    
    if request.method=="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')  
    
        

        user = authenticate(request, email=email, password=password)
        if user is not None:
            if user.is_verified:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, "Please verify your email first.")  
                return redirect('login')
        else:
            messages.error(request, "email or password incorrect")
            return redirect('login')
    return render(request, 'base/login.html')

@login_required(login_url="/login")
def logoutUser(request):
   
    logout(request)
    return redirect('login')


def create_blogs(request):
    return render(request, 'base/create_blogs.html')