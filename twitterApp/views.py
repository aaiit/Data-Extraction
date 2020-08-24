from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Greeting
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from commentsandlikes import comments, likes
from get_tweets import get_tweets_text, get_comments, get_tweets_video
from downloadImages import downloadImages
from fire import database

def table(request):
	a=request.GET.get("a")
	print(a)
	js=database.child("data/json/"+a).get().val()
	if js==None:
		return HttpResponse("data not found")
	js=json.loads(js)
	print(js)
	keys=list(js[0].keys())
	def e(l):
		Q=[]
		for i in l:
			Q.append(l[i])
		return Q
	lignes=[]
	for j in js:
		lignes.append(list(e(j)))
	return render(request, "table.html",{"C":keys,"data":lignes})


def index(request):
	return render(request, "index.html")



@csrf_exempt 
def formText(request):
	if request.method=='POST':
		fields=json.loads(request.body)
		print(fields)
		return HttpResponse(get_tweets_text(fields))
	return render(request, "f0.html")


@csrf_exempt 
def formImage(request):
	if request.method=='POST':
		fields=json.loads(request.body)
		type=fields["type"]
		print(fields)
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



def google(request):
	return redirect('https://google.com')