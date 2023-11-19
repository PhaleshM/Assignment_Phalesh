from django.contrib import admin
from .models import Log
# Register your models here.

class LogModelAdmin(admin.ModelAdmin):
    list_display=('level','message','resourceId')

admin.site.register(Log,LogModelAdmin)