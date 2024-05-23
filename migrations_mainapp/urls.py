from django.contrib import admin
from django.urls import path, include
from .views import PostMongoCollectionVIew, PostPostgresCollectionView

urlpatterns = [
    path('postSociosMongo/', PostMongoCollectionVIew.as_view(), name="postSociosMongoApiView"),
    path('postSociosPostgres/', PostPostgresCollectionView.as_view(), name="postSociosPostgresApiView"),
]
