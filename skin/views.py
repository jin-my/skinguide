from django.shortcuts import render

from .models import Photo, Product #model에 있는 클래스를 import

# Create your views here.
def skin(request):
    return render(request, 'skintest.html')

def skincheck(request):
    return render(request, 'skincheck.html')

# 사진 불러와서 출력하는 용도 객체 만들기

def image(request):
    images = Photo.objects #images 라는 객체는 저장하고, {}를 html에 넘겨준다

    return render(req, 'skincheck.html', {'images'} : iamges) # key 값을 들여움
