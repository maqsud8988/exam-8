from django.contrib import admin
from services.models import Services
from import_export.admin import ImportExportModelAdmin

@admin.register(Services)
class ServicesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ("servise_name",)

    list_display = ("id", "servise_name")
    list_filter = ("servise_name",)
