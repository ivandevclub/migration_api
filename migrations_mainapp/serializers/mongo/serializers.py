from rest_framework.serializers import ModelSerializer
from ...models.mongo.models import Socio

class SocioSerializer(ModelSerializer):
    class Meta:
        model = Socio
        fields = "__all__"

    def create(self, validated_data):
        return Socio.objects.using('default').create(**validated_data)