from django.shortcuts import render
from django.http import HttpResponse
import json
from .Twitter.Wrapper import search_for_tweets
from .models import Greeting
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from twitterApp.commentsandlikes import comments, likes
from twitterApp.get_tweets import get_tweets_text, get_comments, get_tweets_video
from twitterApp.downloadImages import downloadImages
from fire import database, upload, uploadfilds ,getrandomid, savefile, sendUpdate
import pandas as pd
from datetime import datetime

def home(request):
    return render(request,"home.html")
def graph(request, id=""):
    a = id  
    st = database.child("data/json/" + a).get().val()
    js = st
    if js == None:
        return redirect('/')
    results = json.loads(js)

    images = results["graph"]
    js = list(results["table1"].values() )

    keys = list(js[0].keys())

    def e(l):
        Q = []
        for i in l:
            Q.append(l[i])
        return Q

    lignes = []
    for j in js:
        lignes.append(list(e(j)))

    keys1, lignes1 = keys, lignes

    js = list(results["table2"].values() )
    keys = list(js[0].keys())
    lignes = []
    for j in js:
        lignes.append(list(e(j)))
    keys2, lignes2 = keys, lignes

    # images=[string.encode(encoding='UTF-8',errors='strict') for string in images]
    # print(images)
    para = {"JSON":st,"C1": keys1, "data1": lignes1, "C2": keys2, "data2": lignes2, "images": images}
    return render(request, "graph.html", para)
def table(request, id=""):
    a = id  # request.GET.get("a")
    st = database.child("data/json/" + a).get().val()
    print("++++",st)
    js = st
    if js == None:
        return redirect('/')
    js = json.loads(js)



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

    pd.DataFrame(js).to_excel(r'%s.xlsx'%(a),index=False)
    
    return render(request, "table.html", {"xlsx":savefile('%s.xlsx'%(a)),"CSV":pd.DataFrame(js).to_csv(index=False),"C": keys, "data": lignes, "JSON": st, "id": a})
def index(request):
    return render(request, "index.html")
@csrf_exempt
def formText(request):
    if request.method == 'POST':
        fields = json.loads(request.body)
        print(fields)
        f = fields
        type = fields["type"]
        if type == "graphe":
            r = json.dumps(search_for_tweets(fields,request),default=str)
            id = upload(r)
            type="graph"
        else:
            id = get_tweets_text(fields)
            type="data"
        print("id is "+id)
        return HttpResponse(id)
    return render(request, "f0.html")
# ++
@csrf_exempt
def formImage(request):
    if request.method == 'POST':
        fields = json.loads(request.body)
        type = fields["type"]
        print(fields)
        return HttpResponse(json.dumps(downloadImages(fields)))
    return render(request, "fimage.html")


# @csrf_exempt
# def formVideo(request):
#     if request.method == 'POST':
#         fields = json.loads(request.body)
#         print(fields)
#         id=upload(json.dumps(get_tweets_video(fields)))
#         return HttpResponse(id)
#     return render(request, "fvideo.html")
@csrf_exempt
def formVideo(request):
    if request.method == 'POST':
        fields = json.loads(request.body)
        print(fields)
        return HttpResponse(get_tweets_video(fields))
    return render(request, "fvideo.html")


@csrf_exempt
def f1(request):
    if request.method == 'POST':
        fields = json.loads(request.body)
        f = fields
        type = fields["type"]
        print(fields)
        id = get_comments(fields)
        return HttpResponse(id)
    return render(request, "f1.html")


@csrf_exempt
def f2(request):
    if request.method == 'POST':
        fields = json.loads(request.body)
        type = fields["type"]
        print(fields)
        return HttpResponse(likes(fields))
    return render(request, "f2.html")


@csrf_exempt
def f3(request):
    if request.method == 'POST':
        fields = json.loads(request.body)
        type = fields["type"]
        print(fields)
        return HttpResponse(comments(fields))
    return render(request, "f3.html")



def standardOperators(request):
    return render(request, "standard-operators.html")
