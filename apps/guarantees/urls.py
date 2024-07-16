from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.guarantees.views import GuaranteesDetailViewSet, GuaranteesUpdateViewSet, GuaranteesDeleteViewSet, \
    GuaranteesCreateViewSet, GuaranteesListViewSet

router = DefaultRouter()

urlpatterns = [
                  path('', GuaranteesListViewSet.as_view(),
                       name='guarantees-list'),
                  path('create/', GuaranteesCreateViewSet.as_view(),
                       name='guarantees-create'),
                  path('detail/<int:pk>/', GuaranteesDetailViewSet.as_view(),
                       name='guarantees-detail'),
                  path('update/<int:pk>/', GuaranteesUpdateViewSet.as_view(),
                       name='guarantees-update'),
                  path('delete/<int:pk>/', GuaranteesDeleteViewSet.as_view(),
                       name='guarantees-delete')
              ] + router.urls
