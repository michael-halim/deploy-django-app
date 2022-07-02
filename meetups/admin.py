from django.contrib import admin
from .models import Meetup,Location,Participant

class MeetuplAdmin(admin.ModelAdmin):
    list_display = ('title', 'date','location',)
    list_filter = ('location',)
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Meetup,MeetuplAdmin)
admin.site.register(Location)
admin.site.register(Participant)
