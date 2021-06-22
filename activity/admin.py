from django.contrib import admin
from django.db import models
from .models import DetailActivity, RawActivity, SleepEvent
# Register your models here.

class SleepAdmin(admin.ModelAdmin):
    readonly_fields = ('time_end',)


admin.site.register(RawActivity)
admin.site.register(DetailActivity)
admin.site.register(SleepEvent,SleepAdmin)