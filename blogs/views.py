from django.shortcuts import render
from datetime import datetime

# Create your views here.
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

from .models import Blogs

# Create your views here.
def landing(request) :
    return render(request,'landingpage.html')

def log_in(request) :
    if request.method == 'POST' :
        username=request.POST['username']
        password=request.POST['password']
        
        user=auth.authenticate(username=username,password=password)
        if user is not None :
            auth.login(request,user)
            return redirect('/')
        else :
            messages.info("Invalid credintals")
            return redirect('login')
    
    return render(request,'login.html')  

    

def sign_up(request) :
    if request.method == 'POST' :
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['confirm-password']

        if password == password2 :
            if User.objects.filter(email=email).exists() :
                messages.info("Email is already exists")
                return redirect('signup')
            elif User.objects.filter(username=username).exists() :
                messages.info("Username already exists")
                return redirect('signup')
            else :
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else :
            messages.info("Passwords doesn't match")
            return redirect('signup') 
    else :
        return render(request,'signup.html')    

def explore(request) :
    blogs=Blogs.objects.all()
    return render(request,'explore.html',{'blogs' : blogs})  

def post(request,id) :
    blogs = Blogs.objects.get(id=id)
    #blogs = get_object_or_404(Blogs, pk=pk)
    return render(request,'fullblog.html',{'blogs' : blogs})

def log_out(request):
    auth.logout(request)
    return redirect('/')

def write(request):
    if request.method == 'POST' :
        title=request.POST['title']
        body=request.POST['body']
        blog=Blogs.objects.create(title=title,body=body)
        return redirect('explore')
    else:
        return render(request,'writing.html')
    



    
