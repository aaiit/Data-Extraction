from django.shortcuts import render
from django.http import HttpResponse
import json
from .Twitter.Wrapper import search_for_tweets
from .models import Greeting
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from commentsandlikes import comments, likes
from get_tweets import get_tweets_text, get_comments, get_tweets_video
from downloadImages import downloadImages
from fire import database,upload,uploadfilds

def history(request):
	return HttpResponse(request.session['coco'])
	
def graph(request,id=""):
	a=id#request.GET.get("a")
	st=database.child("data/graph/"+a).get().val()
	js=st
	if js==None :
		return redirect('/')
	results=json.loads(js)
	images=results["graph"]
	js=results["table1"]

	keys=list(js[0].keys())
	def e(l):
		Q=[]
		for i in l:
			Q.append(l[i])
		return Q
	lignes=[]
	for j in js:
		lignes.append(list(e(j)))
	keys1,lignes1=keys,lignes

	js=results["table2"]
	keys=list(js[0].keys())
	lignes=[]
	for j in js:
		lignes.append(list(e(j)))
	keys2,lignes2=keys,lignes

	para={"C1":keys1,"data1":lignes1,"C2":keys2,"data2":lignes2,"images":images}
	return render(request,"graph.html",para)

def table(request,id=""):
	a=id #request.GET.get("a")
	st=database.child("data/json/"+a).get().val()
	js=st
	if js==None :
		return redirect('/')
	js=json.loads(js)
	if(js==[]):return HttpResponse("empty data")
	keys=list(js[0].keys())
	def e(l):
		Q=[]
		for i in l:
			Q.append(l[i])
		return Q
	lignes=[]
	for j in js:
		lignes.append(list(e(j)))
	return render(request, "table.html",{"C":keys,"data":lignes,"JSON":st,"id":a})


def index(request):
	return render(request, "index.html")



@csrf_exempt 
def formText(request):
	if request.method=='POST':
		fields=json.loads(request.body)

		f=fields

		type=fields["type"]
		request.session['coco']=json.dumps(fields)
		if type=="graphe":
			r=json.dumps(search_for_tweets(fields))
			id=upload(r)
			print(">>>>"+r[:100]+"...")
			return HttpResponse(id)
		id=get_tweets_text(fields)

		uploadfilds(json.dumps([f]),"f"+id)

		return HttpResponse(id)
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
		f=fields
		type=fields["type"]
		print(fields)
		id=get_comments(fields)
		uploadfilds(json.dumps([f]),"f"+id)
		return HttpResponse(id)
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



