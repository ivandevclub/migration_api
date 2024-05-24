from django.contrib import admin
from django.urls import path, include
from .views import testdb

urlpatterns = [
    path("test/", testdb)
]
