from django.urls import path
from skin import views
app_name = "skin"
urlpatterns = [
    path('', views.skin, name='skin'),
    path('skincheck/', views.skincheck, name = 'skincheck'),
]