from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Greeting
from django.views.decorators.csrf import csrf_exempt

from Core import *
from Sabah import downloadImages
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

def formImage(request):
	# return HttpResponse('Hello from Python!')
	if request.method=='POST':
		fields=json.loads(request.body)
		downloadImages(fields)
		zip_file = open(path_to_file, 'r')
		response = HttpResponse(zip_file, content_type='application/force-download')
		response['Content-Disposition'] = 'attachment; filename="%s"' % 'Imagesdownl.zip'
		return response
		
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
