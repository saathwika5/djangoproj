from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from mycontacts import views
urlpatterns = [
    url(r'save.*', views.save, name='save'),
    url(r'delete.*', views.delete, name='delete'),
]