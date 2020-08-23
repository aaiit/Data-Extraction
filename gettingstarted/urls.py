from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views


urlpatterns = [
    path("", hello.views.index),
    path("form1/", hello.views.formText),
    path("form2/", hello.views.formImage),
    path("form3/", hello.views.formVideo),
    path("standard-operators/", hello.views.standardOperators),
    path("f1/", hello.views.f1),
    path("f2/", hello.views.f2),
    path("f3/", hello.views.f3),
    path("t/", hello.views.table, ),

]
