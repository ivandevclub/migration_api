from django.contrib import admin
from django.urls import path, include
from .views import PostMongoCollectionVIew, PostPostgresCollectionView, MigrationApiView

urlpatterns = [
    path('postSociosMongo/', PostMongoCollectionVIew.as_view(), name="postSociosMongoApiView"),
    path('postSociosPostgres/', PostPostgresCollectionView.as_view(), name="postSociosPostgresApiView"),
    path('migrationView/', MigrationApiView.as_view(), name="migrationApiView"),
]
