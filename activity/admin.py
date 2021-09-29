from django.contrib import admin
from .models import Activity, SleepEvent, Survey, UsageData
# Register your models here.

class SleepAdmin(admin.ModelAdmin):
    readonly_fields = ('time_end',)


admin.site.register(Activity)
admin.site.register(Survey)
admin.site.register(UsageData)

admin.site.register(SleepEvent,SleepAdmin)