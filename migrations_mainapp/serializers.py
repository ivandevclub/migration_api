from rest_framework.serializers import ModelSerializer
from .models import Socio

class SocioSerializer(ModelSerializer):
    class Meta:
        model = Socio
        fields = "__all__"
