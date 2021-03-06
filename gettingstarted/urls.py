from django.urls import path, include
from django.contrib import admin
admin.autodiscover()
import twitterApp.views
import youtubeApp.views
from django.shortcuts import render

urlpatterns = [
	path("", twitterApp.views.home),

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
    
    path("data/<str:id>", twitterApp.views.table, ),
    path("graph/<str:id>", twitterApp.views.graph, ),

    #path("corona/", youtubeApp.views.Corona, ),

]
