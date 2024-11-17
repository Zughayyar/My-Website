from django.shortcuts import render, HttpResponse, redirect
from . import models

# Create your views here.
def wall(request):
    if request.session['is_logged_in'] is True:
        logged_user = models.get_user_by_email(request.session['user_email'])
        context = {
            'user' : logged_user[0],
            'messages': models.get_all_messages()
        }
        return render(request, "wall.html", context)
    else:
        return HttpResponse("Who are you ?!!")

def post_message(request):
    if request.method == "POST":
        logged_user = models.get_user_by_email(request.session['user_email'])
        models.create_message(request.POST, logged_user[0])
        return redirect('/wall')

    else:
        return HttpResponse("Something went wrong!")

def post_comment(request):
    if request.method == "POST":
        logged_user = models.get_user_by_email(request.session['user_email'])
        models.create_comment(request.POST, logged_user[0])
        return redirect('/wall')

    else:
        return HttpResponse("Something went wrong!")