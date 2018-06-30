from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.utils.safestring import mark_safe
import json

def index(request):
    template = loader.get_template('chatter/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def get_room(request, room_name):
    template = loader.get_template('chatter/gbpusd.html')
    context = {
        'room_name_json': mark_safe(json.dumps(room_name))
    }
    return HttpResponse(template.render(context, request))
