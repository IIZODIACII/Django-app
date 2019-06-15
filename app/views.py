from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.shortcuts import render
import requests
import json


def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())


def result(request):
    raw_numbers = request.GET.get('array').split(",")
    array = []
    for i in raw_numbers:
        array.append(int(i))

    post_data = {'target': request.GET.get('average'), 'array_size': request.GET.get(
        'size'), 'numbers': array}
    headers = {'Content-type': 'application/json'}
    print(post_data)

    response = requests.post(
        'https://gp-task-php.herokuapp.com/calc', data=json.dumps(post_data), headers=headers)
    content = json.loads(response.content)

    html = "<!DOCTYPE html><html><head><link href='/static/css/style.css' rel='stylesheet'/></head><body><div class='content'>Result:%s</div></body></html>" % content['result']
    return HttpResponse(html)
