from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response


def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())