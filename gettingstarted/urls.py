from django.urls import path, include
from django.contrib import admin
admin.autodiscover()
import twitterApp.views
import youtubeApp.views
import linkedinApp.views


urlpatterns = [
    path("", twitterApp.views.index),
    path("form1/", twitterApp.views.formText),
    path("form2/", twitterApp.views.formImage),
    path("form3/", twitterApp.views.formVideo),
    path("standard-operators/", twitterApp.views.standardOperators),
    path("f1/", twitterApp.views.f1),
    path("f2/", twitterApp.views.f2),
    path("f3/", twitterApp.views.f3),
    path("t/", twitterApp.views.table, ),
    path("lnkdn/",linkedinApp.views.index),
    path("yt/",youtubeApp.views.index),
]
