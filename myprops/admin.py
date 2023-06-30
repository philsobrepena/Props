from django.contrib import admin
from myprops.models import Props


@admin.register(Props)
class PropAdmin(admin.ModelAdmin):
    list_display = ("item", "description")
