from django.shortcuts import render
from django.http import HttpResponse
from news.models import NewsContent
from django.template import RequestContext, loader
from django.shortcuts import render
from django.shortcuts import *
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from custom_rest.serializers import NewsContentModelSerializer
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser



# Create your views here.
@csrf_exempt
def news_rest_list(request):
	if request.method == 'GET':
		news = NewsContent.objects.all()
		serializer = NewsContentModelSerializer(news, many=True)
		return JSONResponse(serializer.data)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		news = NewsContentModelSerializer(data=data)
		if news.is_valid():
			news.save()
			return JSONResponse(serializer.data, status=201)
		return JSONResponse(serializer.errors, status=400)

class NewsViewSet(viewsets.ModelViewSet):
    
	queryset = NewsContent.objects.all()
	serializer_class = NewsContentModelSerializer



class JSONResponse(HttpResponse):
    
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)

# Create your views here.
