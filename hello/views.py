from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Greeting
from django.views.decorators.csrf import csrf_exempt
import zipfile

from Ayoub import gettweetstext
from Sabah import downloadImages
from fire import getUrlOfZip

def index(request):
	return render(request, "choose.html")

@csrf_exempt 
def formText(request):
	if request.method=='POST':
		fields=json.loads(request.body)
		#fields = {'q': 'covid19', 'lang': 'en', 'result_type': 'popular',"len":2}
		return HttpResponse(gettweetstext(fields))
	return render(request, "form1.html")


@csrf_exempt 
def formImage(request):
	if request.method=='POST':
		fields=json.loads(request.body)
		type=fields["type"]
		print(fields)
		path_to_file="hello/static/ImagesDownload.zip"
		if type=="txt":
			return HttpResponse(downloadImages(fields))
		downloadImages(fields)
		return HttpResponse(getUrlOfZip(path_to_file))
		
	return render(request, "fimage.html")

def formVideo(request):
	return render(request, "fvideo.html")


def f1(request):
	if request.method=='POST':
		fields=json.loads(request.body)
		type=fields["type"]
		print(fields)
		return HttpResponse("ok")
	return render(request, "f1.html")


def f2(request):
	if request.method=='POST':
		fields=json.loads(request.body)
		type=fields["type"]
		print(fields)
		return HttpResponse("ok")
	return render(request, "f2.html")


def f3(request):
	if request.method=='POST':
		fields=json.loads(request.body)
		type=fields["type"]
		print(fields)
		return HttpResponse("ok")
	return render(request, "f3.html")

def standardOperators(request):
	return render(request, "standard-operators.html")
