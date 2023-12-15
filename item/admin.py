from django.contrib import admin

from .models import Category, Item,UserActivity

# Register models
admin.site.register(Category)
admin.site.register(Item)
# admin.site.register(UserActivity)
from django.contrib import admin
from django.http import HttpResponse
from openpyxl import Workbook
from .models import UserActivity
from .models import UserPreferences
admin.site.register(UserPreferences)

# @admin.register(UserActivity)
class UserActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'product_category', 'price_range', 'timestamp')
    list_filter = ('product_category', 'price_range', 'timestamp')
    search_fields = ('product_category', 'price_range')

    def export_to_excel(self, request, queryset):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="user_activity_export.xlsx"'

        # Create a new Excel workbook
        wb = Workbook()
        ws = wb.active

        # Define column headers
        ws.append(['User', 'Product Category', 'Price Range', 'Timestamp'])

        # Fetch data and write to Excel
        for obj in queryset:
            ws.append([obj.user.username, obj.product_category, obj.price_range, obj.timestamp])

        # Save the workbook content to the response
        wb.save(response)
        return response

    export_to_excel.short_description = "Export selected as Excel"  # Action description

# Register your model and admin class
admin.site.register(UserActivity, UserActivityAdmin)
