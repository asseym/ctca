'''
Created on Feb 19, 2012

@author: asseym
'''
from .models import *
from django.contrib import admin

class CommunicationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,     {'fields':['title','communication_type','communication_date','objectives','channel','target_audience','recommendations','challenges','lessons', 'action_points', 'remarks', 'attachments']}),
        ('Publication Status', {'fields': ['entry_status'], 'classes': ['collapse']}),
    ]

    list_display = ('title', 'communication_type', 'communication_date', 'channel', 'entry_status')
    list_filter = ['communication_date']
    search_fields = ['title', 'target_audience', 'recommendations']
    list_per_page = 20

admin.site.register(Communication, CommunicationAdmin)
