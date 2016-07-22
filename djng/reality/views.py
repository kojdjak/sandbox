from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse

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


def add(request):
    new_reality = request.POST['add_reality']
    if new_reality:
        house = House()
        house.name = new_reality
        house.save()
    return HttpResponseRedirect(reverse('reality:index'))




from django .contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ( 'name')


from django.contrib.auth.models import User, Group
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

