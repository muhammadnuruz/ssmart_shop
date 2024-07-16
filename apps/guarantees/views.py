from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.permissions import AllowAny

from apps.guarantees.models import Guarantees
from apps.guarantees.serializers import GuaranteesSerializer, GuaranteesCreateSerializer


class GuaranteesListViewSet(ListAPIView):
    queryset = Guarantees.objects.all()
    serializer_class = GuaranteesSerializer


class GuaranteesCreateViewSet(CreateAPIView):
    queryset = Guarantees.objects.all()
    serializer_class = GuaranteesCreateSerializer
    permission_classes = [AllowAny]


class GuaranteesDeleteViewSet(DestroyAPIView):
    queryset = Guarantees.objects.all()
    serializer_class = GuaranteesSerializer
    permission_classes = [AllowAny]


class GuaranteesUpdateViewSet(UpdateAPIView):
    queryset = Guarantees.objects.all()
    serializer_class = GuaranteesCreateSerializer
    permission_classes = [AllowAny]


class GuaranteesDetailViewSet(RetrieveAPIView):
    queryset = Guarantees.objects.all()
    serializer_class = GuaranteesSerializer
    permission_classes = [AllowAny]
