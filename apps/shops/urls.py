from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.shops.views import ShopsDetailViewSet, ShopsUpdateViewSet, ShopsDeleteViewSet, \
    ShopsCreateViewSet, ShopsListViewSet

router = DefaultRouter()

urlpatterns = [
                  path('', ShopsListViewSet.as_view(),
                       name='shops-list'),
                  path('create/', ShopsCreateViewSet.as_view(),
                       name='shops-create'),
                  path('detail/<int:pk>/', ShopsDetailViewSet.as_view(),
                       name='shops-detail'),
                  path('update/<int:pk>/', ShopsUpdateViewSet.as_view(),
                       name='shops-update'),
                  path('delete/<int:pk>/', ShopsDeleteViewSet.as_view(),
                       name='shops-delete')
              ] + router.urls
