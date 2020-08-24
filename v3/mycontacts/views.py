from django.shortcuts import render

# Create your views here.
def add(requests):
    render(requests, 'mycontacts/add.html',{})
def show(requests):
    render(requests, 'mycontacts/show.html',{})