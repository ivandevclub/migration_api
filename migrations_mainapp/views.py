from django.shortcuts import render
from django.db import connections
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from .serializers.mongo.serializers import SocioSerializer
from .models.mongo.models import Socio

class GetCollectionView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SocioSerializer
    
    def get(self, request):
        try:
            socios_instance = Socio.objects.all()
            paginator = LimitOffsetPagination()
            paginated_data = paginator.paginate_queryset(socios_instance, request, view=self)
            
            if paginated_data is not None:
                serialized_data = self.serializer_class(instance=paginated_data, many=True)
                return paginator.get_paginated_response(serialized_data.data)
            else:
                return Response("No data found", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class GetPostgresColectionView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def get(self,request):
        try:
                #set the main cursor
            with connections['postgres'].cursor() as cursor:
                cursor.execute("SELECT * FROM accesos.accesos;")
                results = cursor.fetchall()
                # print(f'CURRENT RESULTS => ${str(results)}')
            if (results is not None):
                paginator = LimitOffsetPagination()
                paginated_data = paginator.paginate_queryset(results, request, view=self)
                return Response(paginated_data, status=status.HTTP_200_OK)
            return Response("No data yet", status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            

            

    
