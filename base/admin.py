from django.contrib import admin
from .models import Event, Registrant
# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """
    EventAdmin class customize admin panel for Event model.
    """
    list_display = ['type','title', 'owner', 'held',
     'location', 'capacity', 'enrolled', 'date_time']
    list_filter = ['type', 'owner', 'held']
    search_fields = ['type', 'title', 'owner__username',
     'held', 'location', 'capacity']
    ordering = ['date_time', 'held']

@admin.register(Registrant)
class RegistrantAdmin(admin.ModelAdmin):
    """
    RegistrantAdmin class customize admin panel for Event model.
    """
    list_display = ['first_name', 'last_name', 'event',
     'student_id', 'university', 'phone_number']
    list_filter = ['event__type']
    search_fields = ['first_name', 'last_name', 'event__type',
     'event__title', 'student_id', 'university']
    ordering = ['event__date_time']
    