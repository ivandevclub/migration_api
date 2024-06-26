from django.shortcuts import render
from rest_framework.exceptions import ValidationError
import logging
from django.db import transaction
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
        data = SocioPg.objects.all()
        serialized_data = self.serializer_class(data, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
        
    def post(self,request):
        if (not request.data):
            return Response({"error": "Data no puede estar vacio"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            print(request.data)
            serialized_data = self.serializer_class(data=request.data)
            if serialized_data.is_valid():
                print("paso la serializacion!")
                serialized_data.save()
                return Response("Recurso creado con exito en Postgresql", status=status.HTTP_201_CREATED)
            return Response({"error": serialized_data.errors}, status=status.HTTP_400_BAD_REQUEST)            
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class MigrationApiView(APIView):
    permission_classes = [permissions.AllowAny]
    mongo_serializer_class = SocioSerializer
    postgre_serializer_class = SocioPgSerializer
    def post(self,request):
        if (not request.data):
            return Response({"error": "Data no puede estar vacio"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            #validar campos de mongo
            mongo_serialized_data = self.mongo_serializer_class(data=request.data)
            mongo_serialized_data.is_valid(raise_exception=True)
            
            #validar campos de postgresql
            postgre_serialized_data = self.postgre_serializer_class(data=request.data)
            postgre_serialized_data.is_valid(raise_exception=True)
            
            with transaction.atomic():
                mongo_serialized_data.save()
                postgre_serialized_data.save()
                
            return Response({"Message": "Recursos creados correctamente!"}, status=status.HTTP_201_CREATED)
        
        except ValidationError as e:
            logging.error("Error en la validacion de los datos", str(e), exc_info=True)
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
                    
        except Exception as e:
            logging.error("Error en la creacion de los recursos", str(e), exc_info=True)
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
        
            
        