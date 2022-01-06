from django.db import models
from django.shortcuts import render
from django.http import StreamingHttpResponse, HttpResponseRedirect, HttpResponse
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import datetime
from django.db.models import Q

from operator import itemgetter

from .models import History, Service
uri = 'bolt://infra.iis.nsk.su'
user="neo4j"
password="pupil-flute-lunch-quarter-symbol-1816"



# API IMPORTS
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny


@api_view(['GET', ])
@permission_classes((AllowAny,))
def getServices(request):
    result = []
    
    for s in Service.objects.all():
        temp = {}
        temp['title'] = s.title
        temp['decs'] = s.decs
        temp['price'] = s.price
        if s.img:
            temp['img'] = s.img.url
        else:
            temp['img'] = ''
        result.append(temp)

    return Response(result)

@api_view(['GET', ])
@permission_classes((AllowAny,))
def getHistory(request):
    result = []
    
    for s in History.objects.all():
        temp = {}
        temp['title'] = s.title
        temp['decs'] = s.decs
        if s.img:
            temp['img'] = s.img.url
        else:
            temp['img'] = ''

        result.append(temp)

    return Response(result)