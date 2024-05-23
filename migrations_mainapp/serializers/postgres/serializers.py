from rest_framework.serializers import ModelSerializer
from ...models.postgres.models import SocioPg

class SocioPgSerializer(ModelSerializer):
    class Meta:
        model = SocioPg
        fields = "__all__"