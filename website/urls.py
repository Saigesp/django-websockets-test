from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [

    # POLLS
    url(r'^index/$', views.index, name="index"),
    
    # OPENSESAME
    url(r'^opensesame/', admin.site.urls),
]