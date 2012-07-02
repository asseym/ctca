'''
Created on Feb 19, 2012

@author: asseym
'''
from .models import *
from django.contrib import admin

class TechnicalAssistanceFundersInline(admin.TabularInline):
    model = TechnicalAssistanceFunders
    extra = 3
    
class TechnicalAssistanceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['activity', 'consultant', 'services','duration','objectives', 'process', 'audience', 'outputs', 'ta_type', 'lessons', 'evaluation', 'recommendation', 'attachments']}),
        ('Publication Status', {'fields': ['entry_status'], 'classes': ['collapse']}),
    ]
    list_display = ('ta_type', 'activity', 'consultant', 'duration', 'short_audience', 'attachment', 'entry_status')
    list_filter = ['ta_type']
    search_fields = ['activity', 'services', 'objectives']
    list_per_page = 20
    inlines = [TechnicalAssistanceFundersInline]
        
admin.site.register(TechnicalAssistance, TechnicalAssistanceAdmin)