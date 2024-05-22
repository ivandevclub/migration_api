from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from .serializers import SocioSerializer
from .models import Socio

class GetCollectionView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SocioSerializer
    
    def get(self, request):
        try:
            socios_instance = Socio.objects.all()
            if socios_instance is not None:
                serialized_data = self.serializer_class(instance=socios_instance, many=True)
                return Response({"data": serialized_data.data}, status=status.HTTP_200_OK)
            else:
                return Response("No data found", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
