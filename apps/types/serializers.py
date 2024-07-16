from rest_framework import serializers

from apps.types.models import Types


class TypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Types
        fields = "__all__"


class TypesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Types
        exclude = ['created_at', 'updated_at']
