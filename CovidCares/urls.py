"""CovidCares URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import covid_info_pg.urls as covid_info_pg
import vaccine.urls as vaccine_urls
import login.urls as login_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls', namespace='homepage')),
    path('sign-up/', include('sign_up.urls')),
    path('covid-info/', include(covid_info_pg)),
    path('apotik/', include('apotik_app.urls')),
    path('forum/', include('disc_forum.urls')),
    path('vaccine-info/', include(vaccine_urls)),
    path('accounts/login/', include(login_urls)),
]
