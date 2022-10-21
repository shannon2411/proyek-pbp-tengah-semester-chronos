from typing import Reversible
from django.contrib.auth.models import User
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from .models import Comment, Forum
from .forms import CreateComment, CreateDiscForm, UpdateDiscForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user
from django.conf import settings
from django.urls import reverse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers

# Create your views here.

def forum(request):
    disc = Forum.objects.all()
    response = {'disc' : disc}
    return render(request, 'view_forum.html', response)

@login_required() 
def create_disc(request):
    response = {}
    user = get_user(request)
    form = CreateDiscForm(request.POST or None)

    if (form.is_valid and request.method == 'POST'):
        temp = form.save(commit=False)
        temp.author = User.objects.get(pk=request.user.id)
        temp.save()
        return HttpResponseRedirect('/forum')
    else:
        response = {'form': form}
        return render(request, 'disc_form.html', response)

@login_required()
def add_reply(request, id):
    response = {}
    user = get_user(request)
    form = CreateComment(request.POST or None)

    if (form.is_valid and request.method == 'POST'):
        temp = form.save(commit=False)
        temp.author = User.objects.get(pk=request.user.id)
        temp.post = Forum.objects.get(id=id)
        temp.save()
        return HttpResponseRedirect('/forum')
    else:
        response = {'form': form}
        return render(request, 'reply_form.html', response)


@login_required()  
def edit_post(request, id):
    response = {}
    user = get_user(request)
    
    form_disc = get_object_or_404(Forum, id=id)
    if request.POST:
        form = UpdateDiscForm(request.POST or None, instance=form_disc)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.save()
            form_disc = temp
            return HttpResponseRedirect('/forum')

    form = UpdateDiscForm(
            initial={
                "title": form_disc.title,
                "message": form_disc.message,
            }
        )
    response['form'] = form
    response['title'] = form_disc.title
    response['message'] = form_disc.message
    return render(request, 'edit_form.html', response)

@login_required()
def del_post(request, id):
    response = {'id': id}

    if request.POST:
        Forum.objects.get(id=id).delete()
        return HttpResponseRedirect('/forum')
    return render(request, 'del_forum.html', response)

@login_required()
def del_rep(request, id):
    response = {'id': id}

    if request.POST:
        Comment.objects.get(id=id).delete()
        return HttpResponseRedirect('/forum')
    return render(request, 'del_rep.html', response)

@csrf_exempt
def get_forum_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)
    
        title = data["title"]
        message = data["message"]
        date = data["date"]

        forum = Forum(title=title, author=User.objects.get(id=id), message=message, date=date)

        forum.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        forum = Forum.objects.all()
        json_forum = serializers.serialize('json', forum)
        return HttpResponse(json_forum, content_type="application/json")

@csrf_exempt
def get_reply_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)
    
        reply = data["reply"]
        repDate = data["repDate"]

        reply = Comment(post=Forum.objects.get(id=id), author=User.objects.get(id=id), reply=reply, repDate=repDate)

        reply.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        reply = Comment.objects.all()
        json_reply = serializers.serialize('json',reply)
        return HttpResponse(json_reply, content_type="application/json")