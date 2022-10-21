from django.urls import path
from .views import index, add_feedback 

app_name = 'homepage'

urlpatterns = [
    path('', index, name="index"),
    path('add_feedback/', add_feedback, name="add_feedback" )
]