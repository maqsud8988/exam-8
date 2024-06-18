from django.contrib import admin
from contact.models import Subscribe_to_Newsletter
from import_export.admin import ImportExportModelAdmin

@admin.register(Subscribe_to_Newsletter)
class ContactAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ("name",)

    list_display = ("id", "name")
    list_filter = ("name",)




