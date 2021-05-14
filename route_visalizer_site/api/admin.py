from django.contrib import admin
import api.models as models

admin.site.register(models.Route)
admin.site.register(models.GPSRecord)
admin.site.register(models.RouteAttributes)
