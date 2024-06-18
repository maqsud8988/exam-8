from django.contrib import admin
from about.models import OurTeam
from import_export.admin import ImportExportModelAdmin

@admin.register(OurTeam)
class OurTeamAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('name',)

    list_display = ('id', 'name')
    list_filter = ('name',)
