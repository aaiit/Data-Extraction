from django.shortcuts import render
from django.http import HttpResponse
import json
from youtubeApp.Youtube.Youtube import *
from django.views.decorators.csrf import csrf_exempt
from fire import upload,uploadfilds
def index(request):
	return render(request,"ytindex.html")

@csrf_exempt
def searchv(request):
	if request.method=='POST':
		fields=json.loads(request.body)
		f=fields
		print(fields)
		fields["type"]="json"
		data=search_videos(fields)
		id=upload(data)
		uploadfilds(json.dumps([f]),"_"+id)
		return HttpResponse(id)
	return render(request,"searchv.html")



@csrf_exempt
def ytcomments(request):
	if request.method=='POST':
		fields=json.loads(request.body)
		f=fields
		print(fields)
		fields["type"]="json"
		data=search_comments(fields)
		id=upload(data)
		uploadfilds(json.dumps([f]),"_"+id)
		return HttpResponse(id)
	return render(request,"ytcomments.html")
