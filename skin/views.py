from django.shortcuts import render, redirect, get_object_or_404

from .models import Photo, Product #model에 있는 클래스를 import
from user.models import User, Userproduct
# Create your views here.
def skin(request):
    return render(request, 'skinmain.html')

def skincheck(request):
    # print(images)
    # print('---') 
    # print(photos)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
    return render(request, 'skincheck.html') 

def userproduct(request):
    images = Product.objects.all()
    photos = Photo.objects.all()
    return render(request, 'userproduct.html', {'images':images, 'photos':photos})

def base(request):
    return render(request, 'base.html')

def select(request):
    return render(request, 'select.html')

def recommend(request):
    images = Product.objects.all()
    photos = Photo.objects.all()
    return render(request, 'recommend.html', {'images':images, 'photos':photos}) 

def skintypetest(request):
    return render(request, 'skintypetest.html')

def yourskintype(request):
    return render(request, 'yourskintype.html')
    
def createskintype(request):
    print(request.method)
    if(request.method == 'POST'):
        post = request.user
        post.skintype = request.POST['stresult']
        # post.body = request.POST['body']
        post.save()
    return redirect('skin:userproduct')

# def update(request, post_id):
#     board = get_object_or_404(Board, pk=post_id)
#     board.title = request.POST['title']
#     board.body = request.POST['body']
#     board.save()
#     return redirect('board:detail', post_id)


# 사진 불러와서 출력하는 용도 객체 만들기

# def image(request):
#     # images = Product.objects.order_by('-created_at') 
#     images = Product.objects.all()
#     print(images)
#     print('aaa')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
#     return render(request, 'skincheck.html', {'images':images}) 
