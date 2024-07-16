from rest_framework import serializers

from apps.shops.models import Shops


class ShopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shops
        fields = "__all__"


class ShopsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shops
        exclude = ['created_at', 'updated_at']
