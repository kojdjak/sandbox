from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


from .models import House

# def index2(request):
#    return HttpResponse("Hello World from Reality!")


def index(request):
    latest_reality_list = House.objects.order_by('id')[:5]
    template = loader.get_template('reality/index.html')
    context = {
        'latest_reality_list': latest_reality_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, reality_id):
    return HttpResponse("You are looking at reality %s." % reality_id)





