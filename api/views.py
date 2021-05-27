from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
def index(requset):
    return  render(requset, 'esss/login.html')

def register(request):
    return  render(request, 'esss//resgister.html')


@login_required(login_url='/home/')
def home(request):
    try:
      user1=request.user
      product = Product.objects.filter(user=user1).count()
      if productcount.objects.filter(user=user1).exists():
          productcount.objects.filter(user=user1).update(productcount=product)
      else:
          prountcount1=productcount(user=user1, productcount=product)
          prountcount1.save()
    except:
        return render(request, "esss/home.html")

    return render(request, "esss/home.html")

def handlesignup(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if len(username)>10:
            messages.error(request, 'Username must be under 10 characters')
            return  redirect('sigin')
        if  not username.isalnum():
            messages.error(request, 'Username Should only contain letters and number ')
            return  redirect('sigin')
        if len(pass1)<=8:
            messages.error(request, "password length to at least a value of 8")
            return  redirect('sigin')
        if pass1!=pass2:
            messages.error(request, 'Password do no match')
            return  redirect('sigin')
        myuser=User.objects.create_user(username, email, pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request, "You account has been successfuly created")
        return redirect("login")
    else:
        return redirect("sigin")

    return render(request , "esss/resgister.html", {'messages' : messages})
def handlelogin(request):
    if request.method=="POST":
        Email=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        user=authenticate(email=Email, password=loginpassword)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')

    return  render(request, "esss/login.html")


def handlelogout(request):
    logout(request)
    messages.success(request,"Successfuly Logged  out" )
    return redirect('login')