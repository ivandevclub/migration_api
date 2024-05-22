from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from .serializers import SocioSerializer
from .models import Socio

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

    
