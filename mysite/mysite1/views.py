from django.shortcuts import render
# Create your views here.

def bootstraps(request):
    return render(request, 'bootstraps.html')

def test():
    return 1