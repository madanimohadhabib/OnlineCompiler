
from django.urls import path , include
from django.views.generic.base import RedirectView
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage

#import views

from . import views



urlpatterns = [

    path('',views.index, name="indexPage"),
    path('runcode',views.runcode, name="runcode"),
     path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("/static/favicon.ico")),
    ),
]
