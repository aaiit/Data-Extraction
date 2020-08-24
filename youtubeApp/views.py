from django.shortcuts import render
from django.http import HttpResponse
import json
from youtubeApp.Youtube import *
from django.views.decorators.csrf import csrf_exempt

def index(request):
	return render(request,"ytindex.html")

@csrf_exempt
def searchv(request):
	if request.method=='POST':
		fields=json.loads(request.body)
		print(fields)
		return HttpResponse(search_videos(fields))
	return render(request,"searchv.html")



@csrf_exempt
def ytcomments(request):
	if request.method=='POST':
		fields=json.loads(request.body)
		print(fields)
		return HttpResponse(search_comments(fields))
	return render(request,"ytcomments.html")