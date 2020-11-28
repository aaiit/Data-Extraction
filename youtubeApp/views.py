from django.shortcuts import render
from django.http import HttpResponse
import json
from youtubeApp.Youtube.Youtube import *
from django.views.decorators.csrf import csrf_exempt
from fire import upload,uploadfilds,savefile
from datetime import datetime
import pandas as pd

def Corona(request):
	js = corona()
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

	pd.DataFrame(js).to_excel(r'corona.xlsx',index=False)
	return render(request, "table.html", {"xlsx":savefile(),"CSV":pd.DataFrame(js).to_csv(index=False),"C": keys, "data": lignes, "JSON": st, "id": "corona"})


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
		return HttpResponse(id)
	return render(request,"ytcomments.html")
