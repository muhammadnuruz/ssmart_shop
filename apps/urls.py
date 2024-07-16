from django.urls import path, include

urlpatterns = [
    path('', include("apps.core.urls")),
    path('telegram-users/', include("apps.telegram_users.urls")),
    path('guarantes/', include("apps.guarantees.urls")),
    path('shops/', include("apps.shops.urls")),
    path('types/', include("apps.types.urls")),
]
