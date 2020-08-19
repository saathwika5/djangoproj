from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(requests):
   return render(requests,'app1/home.html',{'name' : 'sathwika'})
def aboutus(requests):
   return render(requests,'app1/about.html',{'userid' : 'narthaki'})
def myhobbies(requests):
   return render(requests,'app1/hobbies.html')