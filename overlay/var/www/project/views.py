
from django import http
from django.shortcuts import render_to_response

def index(request, template):
    http_host = request.META['HTTP_HOST']
    return render_to_response(template, {'http_host': http_host})
