from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views


urlpatterns = [
    path("", hello.views.index, name="index"),
    path("form1/", hello.views.formText, name="fff"),
    path("form2/", hello.views.formImage, name="fff"),
    path("form3/", hello.views.formVideo, name="fff"),
    path("standard-operators/", hello.views.standardOperators),
    path("f1/", hello.views.f1, name="fff"),
    path("f2/", hello.views.f2, name="fff"),
    path("f3/", hello.views.f3, name="fff"),

]
