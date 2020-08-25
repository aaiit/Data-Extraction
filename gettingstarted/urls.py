from django.urls import path, include
from django.contrib import admin
admin.autodiscover()
import twitterApp.views
import youtubeApp.views

from django.shortcuts import render
def index(request):
	return render(request,"home.html")

urlpatterns = [
	path("", index),

    path("twitter/", twitterApp.views.index),
    path("twitter/form1/", twitterApp.views.formText),
    path("twitter/form2/", twitterApp.views.formImage),
    path("twitter/form3/", twitterApp.views.formVideo),
    path("twitter/standard-operators/", twitterApp.views.standardOperators),
    path("twitter/f1/", twitterApp.views.f1),
    path("twitter/f2/", twitterApp.views.f2),
    path("twitter/f3/", twitterApp.views.f3),

    path("youtube/",youtubeApp.views.index),
    path("youtube/searchv",youtubeApp.views.searchv),
    path("youtube/ytcomments",youtubeApp.views.ytcomments),
    
    path("table/", twitterApp.views.table, ),
    path("graph/", twitterApp.views.graph, ),

    path("lastFields/", twitterApp.views.history, ),

]
