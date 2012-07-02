'''
Created on Feb 19, 2012

@author: asseym
'''
from .models import *
from django.contrib import admin
    
class ActivityAdmin(admin.ModelAdmin):
    fieldsets = [
                    (None,     {'fields':['name','description', 'event_type','event_date','location','objectives','process','audience','number_of_participants','results','recommendations','challenges','lessons','user_evaluation', 'attachments']}),
                    ('Publication Status', {'fields': ['entry_status'], 'classes': ['collapse']}),
    ]

    list_display = ('name', 'event_type', 'event_date', 'location', 'number_of_participants', 'entry_status')
    list_filter = ['event_date']
    search_fields = ['name', 'description']
    list_per_page = 20

admin.site.register(Activity, ActivityAdmin)