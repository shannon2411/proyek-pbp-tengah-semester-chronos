from django.http import response
from django.shortcuts import render, redirect
from .models import Feedback
from .forms import FeedbackForm

def index(request):
    feedbacks = Feedback.objects.all()
    data = {"feedbacks" : feedbacks}
    return render(request, "homepage.html", context=data)

def add_feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect("homepage:index")
