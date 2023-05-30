from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponsePermanentRedirect

# Create your views here.

def index(request):
    print(request.method)
    return HttpResponse("Women site!")


def categories(request, catid):
    return HttpResponse("<h1> Articles by categories! </h1>")

def archive(request):
    return HttpResponsePermanentRedirect('https://poe.com/sage')

