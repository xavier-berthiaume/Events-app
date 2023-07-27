from django.contrib import admin
from .models import Venue, ClubUser, Event

# Register your models here.
# admin.site.register(Venue)
admin.site.register(ClubUser)
# admin.site.register(Event)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')
    ordering = ('name', )

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'event_date', 'manager')
    ordering = ('event_date', )
