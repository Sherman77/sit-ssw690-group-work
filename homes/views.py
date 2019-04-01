
from django.shortcuts import render, get_object_or_404
from .models import Home
import pyrebase

config = {

    'apiKey': "AIzaSyDb9Ez0_utcuIrj8LZz4iyufABSSbpiaGw",
    'authDomain': "quack-f1544.firebaseapp.com",
    'databaseURL': "https://quack-f1544.firebaseio.com",
    'projectId': "quack-f1544",
    'storageBucket': "quack-f1544.appspot.com",
    'messagingSenderId': "740005547099"
  }

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()



def homepage(request):
    services = Home.objects.all()
    return render(request, 'homes/home.html', {'services': services})

def section(request, service_id):
    service_section = get_object_or_404(Home, pk=service_id)
    return render(request, 'homes/section.html', {'service': service_section})

def welcome(request):
    return render(request, 'welcome/welcome.html')

def signin(request):
    return render(request, 'homes/signin.html')

def postsign(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = auth.sign_in_with_email_and_password(email, password)

    return render(request, 'homes/home.html', {'email':email})


