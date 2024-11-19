from django.shortcuts import render, redirect, HttpResponse

def show_books(request):
    return render(request, "books.html")
