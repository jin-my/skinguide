from django.shortcuts import render, redirect, get_object_or_404

from .models import Photo, Product #model에 있는 클래스를 import

# Create your views here.
def skin(request):
    return render(request, 'skintest.html')

def skincheck(request):
    return render(request, 'skincheck.html')

def base(request):
    return render(request, 'base.html')

def select(request):
    return render(request, 'select.html')

# 사진 불러와서 출력하는 용도 객체 만들기

def image(request):
    images = Product.objects.order_by('-created_at') #images 라는 객체는 저장하고, {}를 html에 넘겨준다
    # images = Product.title
    # boards = Board.objects.order_by('-created_at')
    
    return render(request, 'skincheck.html', {'images':images}) # key 값을 들여움

def title(request):
    title = Product.title()
