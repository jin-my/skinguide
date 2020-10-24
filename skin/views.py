from django.shortcuts import render, redirect, get_object_or_404

from .models import Photo, Product #model에 있는 클래스를 import

# Create your views here.
def skin(request):
    return render(request, 'skintest.html')

def skincheck(request):
    images = Product.objects.all()
    photos = Photo.objects.all()
    print(images)
    print('---') 
    print(photos)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
    return render(request, 'skincheck.html', {'images':images, 'photos':photos}) 

def base(request):
    return render(request, 'base.html')

def select(request):
    return render(request, 'select.html')

# 사진 불러와서 출력하는 용도 객체 만들기

# def image(request):
#     # images = Product.objects.order_by('-created_at') 
#     images = Product.objects.all()
#     print(images)
#     print('aaa')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
#     return render(request, 'skincheck.html', {'images':images}) 