from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import fields

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = "__all__"