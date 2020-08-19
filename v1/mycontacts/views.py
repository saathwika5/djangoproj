
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
import operator

def save(requests):
    return HttpResponse('Save the new contacts')
def delete(requests):
    return HttpResponse('Delete the old contacts')
