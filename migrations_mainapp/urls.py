from django.contrib import admin
from django.urls import path, include
from .views import GetMongoCollectionView, GetPostgresColectionView, PostMongoCollectionVIew

urlpatterns = [
    path('sociosMongo/', GetMongoCollectionView.as_view(), name="getSociosApiView"),
    path('sociosPostgres/', GetPostgresColectionView.as_view(), name="getSociosPostgresApiView"),
    path('postSociosMongo/', PostMongoCollectionVIew.as_view(), name="postSociosPostgresApiView"),
    
]
