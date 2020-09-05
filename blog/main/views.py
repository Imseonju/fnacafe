from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def intro(request):
    return render(request, 'intro/intro.html')

def daily(request):
    return render(request, 'daily/daily.html')