from rest_framework import serializers

from apps.guarantees.models import Guarantees


class GuaranteesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guarantees
        fields = "__all__"


class GuaranteesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guarantees
        exclude = ['created_at', 'updated_at']
