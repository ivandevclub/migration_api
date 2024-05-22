from django.contrib import admin
from django.urls import path, include
from .views import GetCollectionView, GetPostgresColectionView

urlpatterns = [
    path('socios/', GetCollectionView.as_view(), name="getSociosApiView"),
    path('sociosPostgres/', GetPostgresColectionView.as_view(), name="getSociosPostgresApiView"),
]
