from django.contrib import admin
from .models import AgentName, AnnouncedLgaResult, AnnouncedPuResult,AnnouncedStateResult, AnnouncedWardResult, LGA, Party, PollingUnit, State, Ward
# Register your models here.

admin.site.register(AgentName)
admin.site.register(AnnouncedLgaResult)
admin.site.register(AnnouncedPuResult)
admin.site.register(AnnouncedStateResult)
admin.site.register(AnnouncedWardResult)
admin.site.register(LGA)
admin.site.register(Party)
admin.site.register(PollingUnit)
admin.site.register(State)
admin.site.register(Ward)
