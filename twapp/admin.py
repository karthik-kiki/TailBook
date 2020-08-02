from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Friends,Pages
from import_export.admin import ImportExportModelAdmin

class FriendsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'gender')
    list_display_links = ('id','name')
    list_per_page = 10
    search_fields = ('name', 'gender')
    list_filter = ('gender', 'date_added')

class PagesAdmin(ImportExportModelAdmin):
    list_display = ('id', 'names')
    list_display_links = ('id','names')
    list_per_page = 10
    search_fields = ('names',)
    list_filter = ('date_addeds',)

admin.site.register(Friends, FriendsAdmin)
admin.site.register(Pages, PagesAdmin)
admin.site.unregister(Group)
