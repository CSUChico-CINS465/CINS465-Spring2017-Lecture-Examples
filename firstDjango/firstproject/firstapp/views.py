from django.shortcuts import render

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate

from .models import *
from .forms import *

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            submit = form.cleaned_data['suggestion']
            suggest = Suggestion(suggestion=submit)
            suggest.save()
            # process the data in form.cleaned_data as required
            form = SuggestionForm()
        else:
            submit = ""
    else:
        form = SuggestionForm()
        submit = ""
    suggestions = Suggestion.objects.all()
    context = {
        'title':"Home",
        'content': suggestions,
        'form':form,
        'submit':submit
        }
    return render(request,'home.html',context)

@csrf_exempt
def suggestions(request):
    if request.method == 'GET':
        suggestions = Suggestion.objects.all()
        suggest = {}
        suggest['suggestions']=[]
        for suggestion in suggestions:
            suggest['suggestions']+=[{
                'id':suggestion.id,
                'suggestion': suggestion.suggestion
                }]
        return JsonResponse(suggest)
    if request.method == 'POST':
        return HttpResponse("POST successful")
    return HttpResponse("404")
        # { 'suggestions':[
        #     {'id': id, 'suggestion': suggestion}
        # ]
        # }

def register(request):
    if request.method == "POST":
        form = registration_form(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password1'))
            #login call back
            return HttpResponseRedirect('/')

    else:
        form = registration_form()
    context = {
        'title':'Register',
        'form':form
    }
    return render(request, 'register.html', context)
