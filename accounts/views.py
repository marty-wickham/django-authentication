# Reverse allows us to pass the name of a URLs instead of a name of a view
from django.shortcuts import render, redirect, reverse
from django.contrib import auth

# Create your views here.
def index(request):
    return render(request, "index.html")


def logout(request):
    auth.logout(request)
    return render(reverse(index))