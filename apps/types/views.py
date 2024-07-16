from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.permissions import AllowAny

from apps.types.models import Types
from apps.types.serializers import TypesSerializer, TypesCreateSerializer


class TypesListViewSet(ListAPIView):
    queryset = Types.objects.order_by('id')
    serializer_class = TypesSerializer


class TypesCreateViewSet(CreateAPIView):
    queryset = Types.objects.all()
    serializer_class = TypesCreateSerializer
    permission_classes = [AllowAny]


class TypesDeleteViewSet(DestroyAPIView):
    queryset = Types.objects.all()
    serializer_class = TypesSerializer
    permission_classes = [AllowAny]


class TypesUpdateViewSet(UpdateAPIView):
    queryset = Types.objects.all()
    serializer_class = TypesCreateSerializer
    permission_classes = [AllowAny]


class TypesDetailViewSet(RetrieveAPIView):
    queryset = Types.objects.all()
    serializer_class = TypesSerializer
    permission_classes = [AllowAny]
