from django.shortcuts import render

# Create your views here.
def index(request):
    appid = ''
    return render(request, 'weatherapp/index.html')
