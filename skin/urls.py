from django.urls import path
from skin import views
app_name = "skin"
urlpatterns = [
    path('', views.skin, name='skin'),
    path('skincheck/', views.skincheck, name = 'skincheck'),
    path('base/', views.base, name = 'base'),
    path('select/', views.select, name = 'select'),
    path('recommend/',views.recommend, name = 'recommend'),
]