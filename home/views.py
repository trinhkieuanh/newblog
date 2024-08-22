from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
   response = HttpResponse()
   response.writelines('<h1>Hallo</h1>')
   response.write('This is my new blog')
   return response
