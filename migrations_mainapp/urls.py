from django.contrib import admin
from django.urls import path, include
from .views import GetCollectionView

urlpatterns = [
    path('socios/', GetCollectionView.as_view(), name="getSociosApiView")
]
