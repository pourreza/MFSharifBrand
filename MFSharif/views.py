from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'base.html', context)

def loadsearch(request):
    context = {}
    return  render(request, 'search.html', context)