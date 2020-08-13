from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views


urlpatterns = [
    path("", hello.views.index, name="index"),
    # path("db/", hello.views.db, name="db"),
    # path("admin/", admin.site.urls),
]
