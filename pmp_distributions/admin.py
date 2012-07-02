'''
Created on Feb 19, 2012

@author: asseym
'''
from .models import *
from django.contrib import admin
    
class DistributionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['distribution_date', 'material', 'recipient','recipient_type']}),
        ('Publication Status', {'fields': ['entry_status'], 'classes': ['collapse']}),
    ]

    list_display = ('distribution_date', 'material', 'recipient', 'recipient_type', 'entry_status')
    list_filter = ['distribution_date']
    search_fields = ['material', 'recipient']
    list_per_page = 20
    
class MaterialAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title', 'material_type', 'material_language','date_developed','objectives', 'purpose','description', 'status', 'distributed_to','number_distributed','reviewed','dissemination_plan','users_evaluation','update_plan','lessons']}),
        ('Publication Status', {'fields': ['entry_status'], 'classes': ['collapse']}),
    ]

    list_display = ('title', 'material_type', 'material_language', 'date_developed', 'status', 'number_distributed', 'entry_status')
    list_filter = ['date_developed']
    search_fields = ['title', 'material_type', 'material_language']
    list_per_page = 20
        
admin.site.register(Material, MaterialAdmin)
admin.site.register(Distribution, DistributionAdmin)