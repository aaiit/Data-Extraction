from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Greeting
from django.views.decorators.csrf import csrf_exempt
from Core import *
from Sabah import downloadImages
import zipfile
# Create your views here.
def index(request):
	return render(request, "choose.html")

@csrf_exempt 
def formText(request):
	# return HttpResponse('Hello from Python!')
	if request.method=='POST':
		fields=json.loads(request.body)
		#fields = {'q': 'covid19', 'lang': 'en', 'result_type': 'popular',"len":2}
		return HttpResponse(test(fields))
	return render(request, "form1.html")


@csrf_exempt 
def formImage(request):
	# return HttpResponse('Hello from Python!')
	if request.method=='POST':
		fields=json.loads(request.body)
		downloadImages(fields)
		path_to_file="downloadImages.zip"
		return HttpResponse("/static/downloadImages.zip")
		
	return render(request, "fimage.html")

def formVideo(request):
	# return HttpResponse('Hello from Python!')
	if request.method=='POST':
		fields=json.loads(request.body)
		#fields = {'q': 'covid19', 'lang': 'en', 'result_type': 'popular',"len":2}
		return HttpResponse(test(fields))
	return render(request, "fvideo.html")

def standardOperators(request):
	return render(request, "standard-operators.html")
