from django.shortcuts import render
from django import http

def index(request):
    http_host = request.META['HTTP_HOST']
    host = {'http_host': http_host}
    return render(request, 'index.html', host)
