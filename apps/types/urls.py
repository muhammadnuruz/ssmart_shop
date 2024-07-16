from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.types.views import TypesDetailViewSet, TypesUpdateViewSet, TypesDeleteViewSet, \
    TypesCreateViewSet, TypesListViewSet

router = DefaultRouter()

urlpatterns = [
                  path('', TypesListViewSet.as_view(),
                       name='types-list'),
                  path('create/', TypesCreateViewSet.as_view(),
                       name='types-create'),
                  path('detail/<int:pk>/', TypesDetailViewSet.as_view(),
                       name='types-detail'),
                  path('update/<int:pk>/', TypesUpdateViewSet.as_view(),
                       name='types-update'),
                  path('delete/<int:pk>/', TypesDeleteViewSet.as_view(),
                       name='types-delete')
              ] + router.urls
