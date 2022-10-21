from django.urls import path
from .views import fetch_data_prov, index, get_covid_ind, get_covid_prov

app_name = "covid_info"

urlpatterns = [
    path('', index, name='index'),
    path('api-indonesia/', get_covid_ind, name='covid-ind'),
    path('get-provinsi/', get_covid_prov, name='covid-prov'),
    path('fetch-provinsi/', fetch_data_prov, name='get-prov')
]