# from django.contrib import admin
# from users.models import User
# from import_export.admin import ImportExportModelAdmin
#
# @admin.register(User)
# class UsersAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#     search_fields = ("name",)
#
#     list_display = ("id", "username")
#     list_filter = ("name",)

from django.contrib import admin
from users.models import User
from import_export.admin import ImportExportModelAdmin

@admin.register(User)
class UsersAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ("username",)  # Ensure search_fields is a tuple

    list_display = ("id", "username", "telegram_id")
    list_filter = ("telegram_id",)

