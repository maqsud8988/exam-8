from django.contrib import admin
from shop.models import Shop
from import_export.admin import ImportExportModelAdmin

@admin.register(Shop)
class ShopAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ("name",)

    list_display = ('id', 'name', 'price')  # Listga qo'shish
    list_filter = ('name',)  # Filtrlash