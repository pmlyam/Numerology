from django.contrib import admin

from .models import PsychomatrixBaseContent, PsychomatrixAdditionalContent, Celebrity

admin.site.register(PsychomatrixBaseContent)
admin.site.register(PsychomatrixAdditionalContent)
admin.site.register(Celebrity)
