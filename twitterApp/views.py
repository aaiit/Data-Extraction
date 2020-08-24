from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Greeting
from django.views.decorators.csrf import csrf_exempt
from Aida import comments, likes
from Ayoub import get_tweets_text, get_comments, get_tweets_video
from Sabah import downloadImages
from fire import database
def table(request):
	a=request.GET.get("a")
	print(a)
	js=database.child("data/json/"+a).get().val()
	if js==None:
		return HttpResponse("data not found")
	js=json.loads(js)
	print(js)
	# js= [{'sort': 'relevance', 'count': '30', 'format': 1, 'video_id': '32161321613', 'keywords': 'great vaccine', 'type': 'json'}]
	keys=list(js[0].keys())
	def e(l):
		Q=[]
		for i in l:
			Q.append(l[i])
		return Q
	lignes=[]
	for j in js:
		lignes.append(list(e(j)))
	# print(lignes)
	return render(request, "table.html",{"C":keys,"data":lignes})


def index(request):
	return render(request, "index.html")



@csrf_exempt 
def formText(request):
	if request.method=='POST':
		fields=json.loads(request.body)
		return HttpResponse(get_tweets_text(fields))
	return render(request, "f0.html")


@csrf_exempt 
def formImage(request):
	if request.method=='POST':
		fields=json.loads(request.body)
		type=fields["type"]
		print(fields)
		path_to_file="hello/static/Imagesdownl.zip"
		return HttpResponse(json.dumps(downloadImages(fields)))

	return render(request, "fimage.html")
@csrf_exempt 
def formVideo(request):
	if request.method=='POST':
		fields=json.loads(request.body)
		print(fields)
		return HttpResponse(get_tweets_video(fields))
	return render(request, "fvideo.html")

@csrf_exempt 
def f1(request):
	if request.method=='POST':
		fields=json.loads(request.body)
		type=fields["type"]
		print(fields)
		return HttpResponse(get_comments(fields))
	return render(request, "f1.html")

@csrf_exempt 
def f2(request):
	if request.method=='POST':
		fields=json.loads(request.body)
		type=fields["type"]
		print(fields)
		return HttpResponse(likes(fields))
	return render(request, "f2.html")

@csrf_exempt 
def f3(request):
	if request.method=='POST':
		fields=json.loads(request.body)
		type=fields["type"]
		print(fields)
		return HttpResponse(comments(fields))
	return render(request, "f3.html")

def standardOperators(request):
	return render(request, "standard-operators.html")
