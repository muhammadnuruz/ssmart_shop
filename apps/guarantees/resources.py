from django.contrib import admin
from django.http import HttpResponse
import xlwt
from apps.guarantees.models import Guarantees


def export_to_excel(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="guarantees.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Guarantees')

    # Write headers
    row_num = 0
    columns = ['ID', 'Shop', 'Type', 'User', 'Serial Number', 'Date of Purchase', 'Validity Period', 'Created At',
               'Updated At']
    for col_num, column_title in enumerate(columns):
        ws.write(row_num, col_num, column_title)

    # Write data rows
    for obj in queryset:
        row_num += 1
        ws.write(row_num, 0, obj.id)
        ws.write(row_num, 1, obj.shop.name)  # Assuming 'name' is a field in your Shops model
        ws.write(row_num, 2, obj.type.name)
        ws.write(row_num, 3, obj.user.full_name)
        ws.write(row_num, 4, obj.serial_number)
        ws.write(row_num, 5, obj.date_of_purchase.strftime('%Y-%m-%d'))
        ws.write(row_num, 6, obj.validity_period.strftime('%Y-%m-%d'))
        ws.write(row_num, 7, obj.created_at.strftime('%Y-%m-%d %H:%M:%S'))
        ws.write(row_num, 8, obj.updated_at.strftime('%Y-%m-%d %H:%M:%S'))

    wb.save(response)
    return response


export_to_excel.short_description = "Export to Excel"
