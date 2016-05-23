from django.shortcuts import render
from django.http import HttpResponse, Http404


def test(request, *args, **kwargs):
    return HttpResponse('OK')

def error404(request):
    raise Http404

# Create your views here.
