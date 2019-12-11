from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def date_app(request):
    s=datetime.datetime.now()
    return HttpResponse(s)
