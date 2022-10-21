from django.urls import include, path
from vaccine.views import index, search

urlpatterns = [
    path('', index, name='index'),
    # add search vaccine through form path
    path('search', search, name='search')
]