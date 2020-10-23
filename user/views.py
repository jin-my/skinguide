from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def user(request):
    return render(request, 'usertest.html')