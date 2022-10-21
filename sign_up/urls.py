from django.urls import path
from . import views

app_name = "sign_up"

urlpatterns = [
    path('', views.Sign_up, name='Sign-Up'),
    path('success/', views.success, name='Sign-Up Successful'),
    path('signup-flutter/', views.signupbyflutter, name='signupApp'),
]