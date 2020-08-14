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

ZIPFILE_NAME = 'Imagesdownl.zip'


def download(request):
    """Download archive zip file of code snippets"""
    response = HttpResponse(content_type='application/zip')
    zf = zipfile.ZipFile(response, 'w')

    # create the zipfile in memory using writestr
    # add a readme
    zf.writestr(README_NAME, README_CONTENT)

    # retrieve snippets from ORM and them to zipfile
    scripts = Script.objects.all()
    for snippet in scripts:
        zf.writestr(snippet.name, snippet.code)

    # return as zipfile
    response['Content-Disposition'] = f'attachment; filename={ZIPFILE_NAME}'
    print("done----<<>")
    return response
@csrf_exempt 
def formImage(request):
	# return HttpResponse('Hello from Python!')
	if request.method=='POST':
		fields=json.loads(request.body)
		print("dow--->>>")
		downloadImages(fields)
		return download(request)
		
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
