from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader


from .models import House

# def index2(request):
#    return HttpResponse("Hello World from Reality!")


def index(request):
    latest_reality_list = House.objects.all()[:5]
#    template = loader.get_template('reality/index.html')
    context = {
        'latest_reality_list': latest_reality_list,
    }
    return render(request, 'reality/index.html', context)
#    return HttpResponse(template.render(context, request))


def detail(request, reality_id):
    try:
        house = House.objects.get(pk=reality_id)
    except House.DoesNotExist:
        raise Http404("House doesn't exist")
    return render(request, 'reality/detail.html', {'reality': house})





