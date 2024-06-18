

from django.contrib import admin
from blog.models import Blog
from import_export.admin import ImportExportModelAdmin

@admin.register(Blog)
class BlogAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ("first_name",)  # Make sure to use a tuple with a comma

    list_display = ("id", "first_name")  # Specify fields to display in the list view
    list_filter = ("first_name",)  # Specify fields for filtering in the admin interface
