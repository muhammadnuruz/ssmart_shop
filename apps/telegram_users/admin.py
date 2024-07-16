from apps.telegram_users.models import TelegramUsers

from django.contrib import admin


class TelegramUsersAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'username', 'phone_number', 'region', 'district', 'chat_id', 'created_at')
    list_filter = ('region', 'district', 'created_at')
    search_fields = ('full_name', 'username', 'phone_number', 'chat_id')


admin.site.register(TelegramUsers, TelegramUsersAdmin)
