from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from skin import views, urls
from .models import User

# from .models import User

# Create your views here.
def user(request):
    return render(request, 'usertest.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username = username, password = password)
        if user is not None:
        #if User.username==username and User.password == password:
            print("인증성공")
            login(request, user)
            return render(request,"skintest.html")
        else:
            print("인증실패")
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect("user:login") 

def signup_view(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        gender = request.POST["gender"]
        skintype = request.POST["skintype"]

        user = User.objects.create_user(username,email,password)
        #user.username = username
        #user.password = password
        user.gender = gender
        user.skintype = skintype
        user.save()
        return redirect("user:login")
    return render(request,"signup.html")
