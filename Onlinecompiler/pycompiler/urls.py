
from django.urls import path , include

#import views

from . import views


urlpatterns = [
    path('',views.index, name="indexPage"),
]