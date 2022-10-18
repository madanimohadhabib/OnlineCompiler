from django.shortcuts import render

# Create your views here.

#create index fuction

def index(request):
    return render(request, 'index.html')
