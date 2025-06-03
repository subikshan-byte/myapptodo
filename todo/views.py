from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todo_user as u
from .models import Task as t
verfiylogin=0
title=""
username=""
def login(request):
    return render(request,"login.html")
def login_button(request):
    global p
    if(request.method=="POST"):
        username=u.objects.filter(username=request.POST.get("username"),password=request.POST.get("password"))
        if(username):
            try:
                p=u.objects.get(username=request.POST.get("username"))
                request.session["username"]=p.pk
                r=t.objects.filter(username=p.pk)
                username=request.POST.get("username")
                return redirect("todo:index")
            except:
                return redirect("odo:index")
        else:
            title="user already taken"
            return render(request,"incorrect.html",{"title":title})
def signup(request):
    return render(request,"signup.html")
def signup_button(request):
    if(request.method=="POST"):
        username=u.objects.filter(username=request.POST.get("username"))
        email=u.objects.filter(password=request.POST.get("email"))
        cpassword=request.POST.get("confirmpassword")
        password=request.POST.get("password")
        if(not username and not email and (cpassword==password)):
            u.objects.create(name=request.POST.get("name"),username=request.POST.get("username"),email=request.POST.get("email"),password=password)
            return render(request,"succesfull.html")
        elif( username or  email):
            title="user name or email already taken"
            return render(request,"incorrect.html",{"title":title})
        else:
            title="password and confirm password doesnot match"
            return render(request,"incorrect.html",{"title":title})
def newtask(request):
    return render(request,"task.html")
def index(request):
    username=request.session.get("username")
    user=u.objects.get(pk=username)
    r=t.objects.filter(username=user) 
    return render(request,"home.html",{"title":request.POST.get("username"),"task":r})   
def f404(request):
    return render(request,"404.html")               
def newtask_button(request):
        if(request.method=="POST"):
            try:
                username=request.session.get("username")
                user=u.objects.get(pk=username)
                task=request.POST.get("title")
                priority=request.POST.get("priority")
                username=request.session.get("username")
                user=u.objects.get(pk=username)
                t.objects.create(username=user,task=task,priority=priority)
                r=t.objects.filter(username=user)
                return redirect("todo:index")              
            except:
                    return redirect("todo:index")