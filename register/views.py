from django.shortcuts import render, redirect, HttpResponse
from . import models
from django.contrib import messages

# Create your views here.
def index(request):
    if 'is_logged_in' not in request.session:
        request.session['is_logged_in'] = False
    return render(request, "index.html")

def success(request):
    if request.session['is_logged_in'] is True:
        logged_user = models.get_user_by_email(request.session['user_email'])
        context = {
            'user' : logged_user[0]
        }
        return render(request, "success.html", context)
    else:
        return HttpResponse("Who are you ?!!")

def register(request):
    if request.method == "POST":
        errors = models.User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            models.create_user(request.POST)
            request.session['is_logged_in'] = True
            if 'user_email' not in request.session:
                request.session['user_email'] = request.POST['email']
            return redirect('/wall')
    else:
        HttpResponse("Something went wrong!")

def signout(request):
    if 'user_email' in request.session:
        request.session['is_logged_in'] = False
        del request.session['user_email']
    return redirect('/')

def login(request):
    if request.method == "POST":
        if models.is_user_exist(request.POST):
            if models.check_login(request.POST):
                request.session['is_logged_in'] = True
                if 'user_email' not in request.session:
                    request.session['user_email'] = request.POST['email']
                return redirect('/wall')
            else:
                errors = {'password' : "Wrong password!"}
                if len(errors) > 0:
                    for key, value in errors.items():
                        messages.error(request, value)
                return redirect('/')
        else:
            HttpResponse("Email not found")    

    else:
        HttpResponse("Something went wrong!")