from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World from Reality!")


def detail(request, reality_id):
    return HttpResponse("You are looking at reality %s." % reality_id)
