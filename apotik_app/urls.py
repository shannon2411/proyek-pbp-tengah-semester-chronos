from django.urls import path
from .views import index, search, search_json

app_name = "apotek"

urlpatterns = [
    path('', index, name = 'index'),
    path('search', search, name = 'search'),
    path('search_json', search_json, name = 'search_json')
    # path('list-apotik', index, name = 'index')
]