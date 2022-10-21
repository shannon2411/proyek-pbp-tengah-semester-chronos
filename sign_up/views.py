from django.shortcuts import render, redirect
from django.http import HttpResponse, response, JsonResponse
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def success(request):
    response = {'name': User.get_username}
    return render(request, 'success.html', response)

def Sign_up(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return success(request)

    context = {'form': form}
    return render(request, 'register.html', context)

@csrf_exempt
def signupbyflutter(request):
    data = json.loads(request.body)
    try:
        newUser = User.objects.create_user(username=data["username"], password=data["password"])
        newUser.save()
        return JsonResponse({"status": "Registration successful", "username": data['username']})
    except:
        return JsonResponse({"errors": "Error Creating User"})