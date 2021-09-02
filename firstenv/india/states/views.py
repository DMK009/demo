from django.shortcuts import render
from django.http import HttpResponse
def sample(request):
    return HttpResponse("<h1>welcome to first demo</h1>")
def addState(request):
    return HttpResponse("<h2>1)Andhra Pradhes<h2>")