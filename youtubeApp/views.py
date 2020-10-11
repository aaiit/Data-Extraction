from django.shortcuts import render
from django.http import HttpResponse
import json
from youtubeApp.Youtube.Youtube import *
from django.views.decorators.csrf import csrf_exempt
from fire import upload,uploadfilds
from datetime import datetime
from corona import corona
import pandas as pd

def Corona(request):
	if "myname" not in request.session:
		request.session["myname"] = getrandomid(10)
	# a = id  # request.GET.get("a")
	# st = database.child("data/json/" + a).get().val()
	# js = st
	# if js == None:
		# return redirect('/')
	js = corona()#json.loads(js)
	st=json.dumps(js)


	if (js == []): return HttpResponse("empty data")
	keys = list(js[0].keys())

	def e(l):
		Q = []
		for i in l:
			Q.append(l[i])
		return Q

	lignes = []
	for j in js:
		lignes.append(list(e(j)))
	return render(request, "table.html", {"CSV":pd.DataFrame(js).to_csv(index=False),"C": keys, "data": lignes, "JSON": st, "id": "corona"})

	# return HttpResponse(corona())
	# return render(request,"ytindex.html")

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
		f=dict(fields)
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
		f=dict(fields)
		print(fields)
		fields["type"]="json"
		data=search_comments(fields)
		id=upload(data)
		uploadfilds(json.dumps([f]),"_"+id)
		h={"time":datetime.now().strftime("%H:%M:%S"),"fields":f,"id":id,"type":"data"}
		savetohistory(request,h)
		
		return HttpResponse(id)
	return render(request,"ytcomments.html")
