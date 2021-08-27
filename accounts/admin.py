from django.contrib import admin
# Register your models here.
from accounts.models import Account,Profile


from import_export.admin import ImportExportModelAdmin


@admin.register(Account)
class BrandAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Profile)