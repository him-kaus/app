from django.contrib import admin
from .models import *


# Register your models here.

class AdminSlot(admin.ModelAdmin):
    list_display = ('Day', 'From', 'To', 'Status')
    list_filter = ('Status', 'Day__Name')


class AdminMeeting(admin.ModelAdmin):
    list_display = ('Slot', 'Client', 'Status')
    list_filter = ('Status',)


class AdminQuery(admin.ModelAdmin):
    list_display = ('Name', 'Email', 'Subject', 'Message')


admin.site.register(Day)
admin.site.register(Shop)
admin.site.register(Slot, AdminSlot)
admin.site.register(Meeting, AdminMeeting)
admin.site.register(CustomerQueries, AdminQuery)
# admin.site.register(Language)
