from rest_framework.serializers import ModelSerializer
from ...models.postgres.models import SocioPg

class SocioPgSerializer(ModelSerializer):
    class Meta:
        model = SocioPg
        fields = "__all__"
    
    def create(self, validated_data):
        return SocioPg.objects.using('postgres').create(**validated_data)