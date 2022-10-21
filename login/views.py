from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def loginbyflutter(request):
    data = json.loads(request.body)
    username = data["username"]
    password = data["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({"status": "logged in", "username": username, "id" : request.user.id})
    else:
        return JsonResponse({"errors": "User Not Found"})


@csrf_exempt
def login_ajax(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("homepage:index")
        return render(request, "login.html")
    else:
        return render(request, "login.html")
    
@csrf_exempt
def logoutbyflutter(request):
    logout(request)
    if request.user.is_authenticated:
        return JsonResponse({"errors": "Log out unsuccessful"})
    else:
        return JsonResponse({"status": "Log out successful"})

def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/')

