from django.contrib import admin

from django.db import models
from .models import Service, History


class ServiceAdmin(admin.ModelAdmin):
    model = Service
class HistoryAdmin(admin.ModelAdmin):
    model = History


admin.site.register(Service, ServiceAdmin)
admin.site.register(History, HistoryAdmin)
