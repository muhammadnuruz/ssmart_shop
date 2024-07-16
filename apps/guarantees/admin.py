from django.contrib import admin

from apps.guarantees.models import Guarantees
from apps.guarantees.resources import export_to_excel


class GuaranteesAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'shop', 'type', 'serial_number', 'date_of_purchase', 'validity_period', 'created_at')
    list_filter = ('user', 'shop', 'type', 'date_of_purchase', 'created_at')
    search_fields = ('id', 'serial_number')
    actions = [export_to_excel]


admin.site.register(Guarantees, GuaranteesAdmin)
