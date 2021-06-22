from report.models import ActivityIndexDiscriptions, Index, Location, ReportToday, Suggestions
from django.contrib import admin

# Register your models here.
admin.site.register(ReportToday)
admin.site.register(Suggestions)
admin.site.register(ActivityIndexDiscriptions)
admin.site.register(Index)
admin.site.register(Location)