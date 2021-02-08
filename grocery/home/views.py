from django.shortcuts import render,redirect
from table.models import *
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.
def log(request):
    for key in list(request.session.keys()):
        if not key.startswith("_"):  # skip keys set by the django system
            del request.session[key]

    if request.method=="POST":
        uname = request.POST.get('uname')
        password = request.POST.get('psw')
        u=user.objects.filter(username=uname,password=password)
        if u.count()>0:
            request.session['id'] = u[0].user_id
            return redirect('http://127.0.0.1:8000/user/')
        else:
            messages.success(request, "Login failed")
    return render(request,'home/login.html')

def signup(request):
    for key in list(request.session.keys()):
        if not key.startswith("_"):  # skip keys set by the django system
            del request.session[key]

    if request.method == 'POST':
        fname = request.POST.get('fname')
        mname = request.POST.get('mname')
        lname = request.POST.get('lname')
        uname = request.POST.get('uname')
        email=  request.POST.get('mail')
        password= request.POST.get('psw')
        u=user.objects.filter(email=email)
        if u.count()>0:
            messages.success(request, "Email already exists")
            return redirect('http://127.0.0.1:8000/signup')

        u = user.objects.filter(username=uname)
        if u.count() > 0:
            messages.success(request, "Username already exists")
            return redirect('http://127.0.0.1:8000/signup')

        u=user(fname=fname,mname=mname,lname=lname,email=email,username=uname,password=password)
        u.save()
        messages.success(request, "Inserted successfully")
        return redirect('http://127.0.0.1:8000/')
    return render(request,'home/signup.html')

def home(request):
    for key in list(request.session.keys()):
        if not key.startswith("_"):  # skip keys set by the django system
            del request.session[key]

    return render(request,'home/home.html')




