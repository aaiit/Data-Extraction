from django.shortcuts import render
from django.http import HttpResponse
import json
from youtubeApp.Youtube.Youtube import *
from django.views.decorators.csrf import csrf_exempt
from fire import upload,uploadfilds
from datetime import datetime


def savetohistory(request,h):
    try:    
        H=json.loads(request.session["history20"])+[h]
    except:
        H=[h]
    request.session["history20"]=json.dumps(H)
    print(">>>",request.session["history20"])

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
		h={"time":datetime.now().strftime("%H:%M:%S"),"fields":f,"id":id,"type":"data"}
		savetohistory(request,h)
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
		h={"time":datetime.now().strftime("%H:%M:%S"),"fields":f,"id":id,"type":"data"}
		savetohistory(request,h)
		
		return HttpResponse(id)
	return render(request,"ytcomments.html")
