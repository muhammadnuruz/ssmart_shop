from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.permissions import AllowAny

from apps.shops.models import Shops
from apps.shops.serializers import ShopsSerializer, ShopsCreateSerializer


class ShopsListViewSet(ListAPIView):
    queryset = Shops.objects.all()
    serializer_class = ShopsSerializer


class ShopsCreateViewSet(CreateAPIView):
    queryset = Shops.objects.all()
    serializer_class = ShopsCreateSerializer
    permission_classes = [AllowAny]


class ShopsDeleteViewSet(DestroyAPIView):
    queryset = Shops.objects.all()
    serializer_class = ShopsSerializer
    permission_classes = [AllowAny]


class ShopsUpdateViewSet(UpdateAPIView):
    queryset = Shops.objects.all()
    serializer_class = ShopsCreateSerializer
    permission_classes = [AllowAny]


class ShopsDetailViewSet(RetrieveAPIView):
    queryset = Shops.objects.all()
    serializer_class = ShopsSerializer
    permission_classes = [AllowAny]
