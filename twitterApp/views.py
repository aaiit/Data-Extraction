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
from fire import database, upload, uploadfilds


def history(request):
    return HttpResponse(request.session['coco'])


def graph(request, id=""):
    # a = id  
    # st = database.child("data/json/" + a).get().val()

    # return HttpResponse(st)    
    # js = st
    # if js == None:
    #     return redirect('/')
    # results = json.loads(js)
    results={"table1": {"67326663": {"id_str": "67326663", "screen_name": "tweetydimes", "created_at": "2009-08-20 14:22:15", "description": "#GG33", "verified": "false", "followers_count": 14244, "friends_count": 1228, "lang": "null", "time_zone": "null"}, "1091046620836360192": {"id_str": "1091046620836360192", "screen_name": "DePavarin", "created_at": "2019-01-31 18:52:39", "description": "", "verified": "false", "followers_count": 6, "friends_count": 41, "lang": "null", "time_zone": "null"}, "756499208262287360": {"id_str": "756499208262287360", "screen_name": "vechelly", "created_at": "2016-07-22 14:40:41", "description": "Believer. Pharmacist. Health counselor. Unapologetic Igbo. #IgboBuIgbo", "verified": "false", "followers_count": 1929, "friends_count": 4999, "lang": "null", "time_zone": "null"}, "1394320674": {"id_str": "1394320674", "screen_name": "stebarg", "created_at": "2013-05-01 10:44:32", "description": "", "verified": "false", "followers_count": 9, "friends_count": 35, "lang": "null", "time_zone": "null"}, "3547141820": {"id_str": "3547141820", "screen_name": "corona_moca1111", "created_at": "2015-09-13 08:20:40", "description": "\u4f01\u753b\u3068\u81ea\u5275\u4f5c\u3068\u96d1\u591a\u3002 \u4f4f\u307f\u5206\u3051\u306b\u671f\u5f85\u3057\u3066\u306f\u3044\u3051\u306a\u3044\u3088\u3002\u30a2\u30a4\u30b3\u30f3\u306f\u9d8f\u898b\u5742\u3055\u3093 \u30ac\u30c1\u3067\u30de\u30a4\u30da\u30fc\u30b9\u3002 @Coron_567\uff08\u30c9\u30c3\u30c8\u7d75\u30a2\u30ab\uff09#Z_\u30c6\u30ec\u30d7\u30b7\u30b3\u30e9_memo", "verified": "false", "followers_count": 304, "friends_count": 499, "lang": "null", "time_zone": "null"}, "92045070": {"id_str": "92045070", "screen_name": "all_rinnn", "created_at": "2009-11-23 15:42:20", "description": "live in meong soul", "verified": "false", "followers_count": 228, "friends_count": 228, "lang": "null", "time_zone": "null"}, "1039483718648221696": {"id_str": "1039483718648221696", "screen_name": "KhairulDaniel67", "created_at": "2018-09-11 12:00:06", "description": "Efforts are better than words", "verified": "false", "followers_count": 121, "friends_count": 103, "lang": "null", "time_zone": "null"}, "3235064428": {"id_str": "3235064428", "screen_name": "Siokalypse", "created_at": "2015-05-05 05:39:37", "description": "Ich humore hier nur so'n Bisschen rum. #Computert\u00fcp #Nervens\u00e4ge #CssVerachter #M\u00e4nnchenVonWeibchen\n\nEigent\u00fcmer des fantastischen https://t.co/nnk0CJtPKf !!", "verified": "false", "followers_count": 338, "friends_count": 281, "lang": "null", "time_zone": "null"}, "1311380571365482498": {"id_str": "1311380571365482498", "screen_name": "alienigenasujo", "created_at": "2020-09-30 19:01:16", "description": "Boca suja", "verified": "false", "followers_count": 2, "friends_count": 32, "lang": "null", "time_zone": "null"}, "602909622": {"id_str": "602909622", "screen_name": "DMichaeld85", "created_at": "2012-06-08 15:07:06", "description": "", "verified": "false", "followers_count": 40, "friends_count": 116, "lang": "null", "time_zone": "null"}}, "table2": {"1313418588015951873": {"created_at": "2020-10-06 09:59:28", "id_str": "1313418588015951873", "full_text": "Good Call... this guy predicted unraveling of mummies and if you see his pinned tweet he predicted the corona virus , never heard of him but he earned a follow https://t.co/7GAPka6g2B", "truncated": "false", "user.id_str": "67326663", "retweet_count": 0, "favorite_count": 0, "lang": "en", "source": "Twitter Web App", "geo": "null", "coordinates": "null", "place": "null", "entities.urls.expanded_url": ["https://twitter.com/Anirudh_Astro/status/1071779340160065536"], "entities.symbols": []}, "1313418585017061376": {"created_at": "2020-10-06 09:59:27", "id_str": "1313418585017061376", "full_text": "@mike_fusco Questo \u00e8 quanto . Ma nel paese di pulcinella e Fabrizio corona non basta . Bisogna pure perdere tempo a cercare se il colpevole \u00e8 colpevole in quanto tale o se lo \u00e8 in quanto sale .", "truncated": "false", "user.id_str": "1091046620836360192", "retweet_count": 0, "favorite_count": 0, "lang": "it", "source": "Twitter for iPhone", "geo": "null", "coordinates": "null", "place": "null", "entities.user_mentions.id_str": ["484082692"], "entities.symbols": []}, "1313418583729414144": {"created_at": "2020-10-06 09:59:27", "id_str": "1313418583729414144", "full_text": "@eze_eche Isi Corona virus \ud83e\udd23\ud83e\udd23", "truncated": "false", "user.id_str": "756499208262287360", "retweet_count": 0, "favorite_count": 0, "lang": "in", "source": "Twitter for Android", "geo": "null", "coordinates": "null", "place": "null", "entities.user_mentions.id_str": ["222533614"], "entities.symbols": []}, "1313418579388358657": {"created_at": "2020-10-06 09:59:26", "id_str": "1313418579388358657", "full_text": "Liked on YouTube: ARD extra: Die Corona-Lage | Keine \u00dcbersterblichkeit in Deutschland | 05.10.2020 https://t.co/4kjBGpB3Pq", "truncated": "false", "user.id_str": "1394320674", "retweet_count": 0, "favorite_count": 0, "lang": "de", "source": "IFTTT", "geo": "null", "coordinates": "null", "place": "null", "entities.urls.expanded_url": ["https://www.youtube.com/watch?v=WoRVAnLvpaY"], "entities.symbols": []}, "1313418569103810560": {"created_at": "2020-10-06 09:59:23", "id_str": "1313418569103810560", "full_text": "@DeusEXZZZ12 @DeusEXZZZ12 \n\u203c\ufe0f\n#Z\u793e_\u93ae\u5727\u30ed\u30fc\u30eb\n\u30c6\u30ec\u30d7\u30b7\u30b3\u30e9\u3001\u308f\u304b\u308a\u307e\u3057\u305f\u3093\u3055\u3093\n\u30bf\u30fc\u30f32\n\u3066\u308c\u3061\u3083\u3093\u219231/100\n\u308f\u304b\u308b\u3055\u3093\u219263/38\n1\u767a\uff01\n\n\u30bf\u30fc\u30f32\u7d42\u4e86", "truncated": "false", "user.id_str": "3547141820", "retweet_count": 0, "favorite_count": 0, "lang": "ja", "source": "Twitter for iPhone", "geo": "null", "coordinates": "null", "place": "null", "entities.hashtags.text": ["Z\u793e_\u93ae\u5727\u30ed\u30fc\u30eb"], "entities.user_mentions.id_str": ["1280850907148640256", "1280850907148640256"], "entities.symbols": []}, "1313418564821377024": {"created_at": "2020-10-06 09:59:22", "id_str": "1313418564821377024", "full_text": "Kenapa pas rapat DPR itu ga ada yg suspek corona sih? Kan sapa tau seruangan jadi kena semua trus pada sekarat gitu, kaya nya menarik.", "truncated": "false", "user.id_str": "92045070", "retweet_count": 0, "favorite_count": 0, "lang": "in", "source": "Twitter for Android", "geo": "null", "coordinates": "null", "place": "null", "entities.symbols": []}, "1313418563097567233": {"created_at": "2020-10-06 09:59:22", "id_str": "1313418563097567233", "full_text": "Sedih banget bayi umur 1 tahun meninggal sebab Cik corona ni. Para mak bapak kalau sayang anak tu simpan anak kat rumah tak payah nak bawak pergi mall kenduri semua", "truncated": "false", "user.id_str": "1039483718648221696", "retweet_count": 0, "favorite_count": 0, "lang": "in", "source": "Twitter for iPhone", "geo": "null", "coordinates": "null", "place": "null", "entities.symbols": []}, "1313418560455270401": {"created_at": "2020-10-06 09:59:21", "id_str": "1313418560455270401", "full_text": "16k Corona F\u00e4lle wurden in Gro\u00dfbritannien nicht an Kontaktverfolger weitergegeben, weil die Exceldatei mit den Infos zu gro\u00df wurde.\n\nTja nun.", "truncated": "false", "user.id_str": "3235064428", "retweet_count": 0, "favorite_count": 0, "lang": "de", "source": "Twitter Web App", "geo": "null", "coordinates": "null", "place": "null", "entities.symbols": []}, "1313418560287510528": {"created_at": "2020-10-06 09:59:21", "id_str": "1313418560287510528", "full_text": "@crisvector @davidmirandario Muitas morte poderiam ser evitadas se n\u00e3o houvesse interfer\u00eancia do STF e tamb\u00e9m os genocidas prefeitos e governadores que desviaram o dinheiro para combater o corona. Muitas outras poderiam ser evitadas se houvesse um tratamento inicial adequado por parte dos m\u00e9dicos.", "truncated": "false", "user.id_str": "1311380571365482498", "retweet_count": 0, "favorite_count": 0, "lang": "pt", "source": "Twitter Web App", "geo": "null", "coordinates": "null", "place": "null", "entities.user_mentions.id_str": ["17984064", "2479861125"], "entities.symbols": []}, "1313418559310176256": {"created_at": "2020-10-06 09:59:21", "id_str": "1313418559310176256", "full_text": "@LeksDogg @PreciousSeloko @Dj_Pios @Ndau_ya_Dzingae @AdvoBarryRoux I said a dangerous wave not covid19...\n\nThe real problem ain't covid19 but they use it a cover up for the real cause... if we were under a real corona there would be no looting of funds\ud83d\udcb0 by the corrupt politicians bcuz they would be fumigating the atmosphere for saving lives\u26b0", "truncated": "false", "user.id_str": "602909622", "retweet_count": 0, "favorite_count": 0, "lang": "en", "source": "Twitter for Android", "geo": "null", "coordinates": "null", "place": "null", "entities.user_mentions.id_str": ["31935840", "1121362123735687168", "131011890", "1071322508505288705", "2449502355"], "entities.symbols": []}}, "graph": ["https://firebasestorage.googleapis.com/v0/b/scrapping-9c4c2.appspot.com/o/images%2FCJxh.jpg?alt=media&token=hhh", "https://firebasestorage.googleapis.com/v0/b/scrapping-9c4c2.appspot.com/o/images%2FMllU.jpg?alt=media&token=hhh", "https://firebasestorage.googleapis.com/v0/b/scrapping-9c4c2.appspot.com/o/images%2FUDhI.jpg?alt=media&token=hhh", "https://firebasestorage.googleapis.com/v0/b/scrapping-9c4c2.appspot.com/o/images%2FevAz.jpg?alt=media&token=hhh", "https://firebasestorage.googleapis.com/v0/b/scrapping-9c4c2.appspot.com/o/images%2F9gLa.jpg?alt=media&token=hhh", "https://firebasestorage.googleapis.com/v0/b/scrapping-9c4c2.appspot.com/o/images%2FIBzY.jpg?alt=media&token=hhh"]}
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

    para = {"C1": keys1, "data1": lignes1, "C2": keys2, "data2": lignes2, "images": images}
    return render(request, "graph.html", para)


def table(request, id=""):
    a = id  # request.GET.get("a")
    st = database.child("data/json/" + a).get().val()
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
    return render(request, "table.html", {"C": keys, "data": lignes, "JSON": st, "id": a})


def index(request):
    return render(request, "index.html")


@csrf_exempt
def formText(request):
    if request.method == 'POST':
        fields = json.loads(request.body)
        print(fields)
        f = fields


        type = fields["type"]
        # request.session['coco']=json.dumps(fields)
        if type == "graphe":
            r = json.dumps(search_for_tweets(fields),default=str)
            id = upload(r)
            print("id"+id)
            return HttpResponse(id)
        id = get_tweets_text(fields)

        uploadfilds(json.dumps([f]), "_" + id)

        return HttpResponse(id)
    return render(request, "f0.html")


@csrf_exempt
def formImage(request):
    if request.method == 'POST':
        fields = json.loads(request.body)
        type = fields["type"]
        print(fields)
        return HttpResponse(json.dumps(downloadImages(fields)))

    return render(request, "fimage.html")


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
        uploadfilds(json.dumps([f]), "_" + id)
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
