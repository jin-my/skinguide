from django.shortcuts import render

# Create your views here.
def skin(request):
    return render(request, 'skintest.html')

def skincheck(request):
    return render(request, 'skincheck.html')