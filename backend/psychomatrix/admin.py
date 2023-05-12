from django.contrib import admin

from .models import (Celebrity, PsychomatrixAdditionalContent,
                     PsychomatrixBaseContent)

admin.site.register(PsychomatrixBaseContent)
admin.site.register(PsychomatrixAdditionalContent)
admin.site.register(Celebrity)
