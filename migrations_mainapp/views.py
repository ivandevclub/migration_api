from django.shortcuts import render
import logging
from django.db import connections
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from .serializers.mongo.serializers import SocioSerializer
from .serializers.postgres.serializers import SocioPgSerializer
from .models.mongo.models import Socio
from .models.postgres.models import SocioPg
        
class PostMongoCollectionVIew(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SocioSerializer
    
    def get(self,request):
        try:
            socios_instance = Socio.objects.all()
            serialized_data = self.serializer_class(socios_instance, many=True)
            return Response(serialized_data.data, status=status.HTTP_200_OK)
        except Exception as e: 
            logging.error("Error en la obtencion de la data", str(e), exc_info=True)
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    def post(self,request):
        try:
            if (not request.data):
                return Response({"message": "Data no puede estar vacio"}, status=status.HTTP_400_BAD_REQUEST)
            serialized_data = self.serializer_class(data=request.data)
            if serialized_data.is_valid():
                print("paso la serializacion")
                serialized_data.save()
                return Response({ "message": "Creado con exito!"}, status=status.HTTP_201_CREATED)  
            logging.error("Error en la serializacion", str(e), exc_info=True) 
            return Response({"error": serialized_data.errors}, status=status.HTTP_400_BAD_REQUEST)     
        except Exception as e:
            logging.error("Error en la creacion de un registro", str(e), exc_info=True)
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
class PostPostgresCollectionView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SocioPgSerializer

    def get(self,request):
        try:
            socios = SocioPg.objects.all()
            serialized_data = self.serializer_class(socios, many=True)
            return Response(serialized_data.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def post(self,request):
        if (not request.data):
            return Response({"error": "Data no puede estar vacio"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            print(request.data)
            serialized_data = self.serializer_class(data=request.data)
            if serialized_data.is_valid():
                print("paso la serializacion!")
                # serialized_data.save()
                return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)