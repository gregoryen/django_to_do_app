from django.shortcuts import render
from . import models

# Create your views here.

def home(request):
    return render(request, template_name='todo/index.html')
