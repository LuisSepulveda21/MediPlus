from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import ips

@admin.register(ips)
class ipsAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')
