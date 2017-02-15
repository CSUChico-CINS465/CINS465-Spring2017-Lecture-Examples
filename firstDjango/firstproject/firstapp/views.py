from django.shortcuts import render

from django.http import HttpResponse

from .models import *

# Create your views here.
def index(request):
    suggestions = Suggestion.objects.all()
    context = {
        'title':"Home",
        'content': suggestions
        }
    return render(request,'home.html',context)
