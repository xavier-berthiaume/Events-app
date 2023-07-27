from django.contrib import admin
from .models import Venue, ClubUser, Event

# Register your models here.
admin.site.register(Venue)
admin.site.register(ClubUser)
admin.site.register(Event)
