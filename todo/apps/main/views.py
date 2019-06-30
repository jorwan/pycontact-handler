from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# hola mundo
def helloworld(request):
    return render(request, 'helloworld.html')