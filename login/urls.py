from django.urls import path
from . import views

app_name = 'login'
urlpatterns = [
    path('', views.login_ajax, name='index'),
    path('login-flutter/', views.loginbyflutter, name='loginApp'),
    path('logout-flutter/', views.logoutbyflutter, name='logoutApp'),
]