from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def index(request):
    return render(request, 'index.html')


def post(request):
    return render(request, '3d.html')