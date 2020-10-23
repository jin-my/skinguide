from django.urls import path
from user import views
app_name = "user"
urlpatterns = [
    #path('', views.user, name='user'),
    path("", views.login_view, name='login'),
    path("logout",views.logout_view, name='logout'),
    path("signup",views.signup_view, name='signup'),
]