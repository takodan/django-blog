from django.shortcuts import render
from django.http import Http404, HttpResponse

# Create your views here.

def index(request):
    try:
        return HttpResponse("This is index")
    except:
        raise Http404()

def posts(request):
    try:
        return HttpResponse("This is posts")
    except:
        raise Http404()

def post_detail(request, slug):
    try:
        return HttpResponse("This is post_detail")
    except:
        raise Http404()