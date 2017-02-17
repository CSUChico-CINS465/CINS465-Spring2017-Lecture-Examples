from django.shortcuts import render

from django.http import HttpResponse

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
