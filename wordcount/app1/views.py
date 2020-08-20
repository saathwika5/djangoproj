from django.shortcuts import render
from django.http import HttpResponse
import operator

# Create your views here.

def home(requests):
    return render(requests, 'app1/home.html')
def count(requests):
    mytext = requests.GET['fulltext'] #get text from the text given in forms
    wcount = len(mytext.split())
    mylist = [('rn1','Samhita'), ('rn2','Sathwika'), ('rn3', 'Renu'), ('rn4', 'Sujitha')]
    return render(requests, 'app1/count.html',{'mycount' : wcount, 'yourlist' : mylist})
