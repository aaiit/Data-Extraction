from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views


urlpatterns = [
    path("", hello.views.index, name="index"),
    path("form/", hello.views.form, name="fff"),
    # path("admin/", admin.site.urls),
]
