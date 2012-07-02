'''
Created on Feb 19, 2012

@author: asseym
'''
from .models import *
from django.contrib import admin

class OperationInline(admin.TabularInline):
    model = Operations
    extra = 3
    
class PartnerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'description', 'membership', 'contact_persons']}),
        ('Publication Status', {'fields': ['entry_status'], 'classes': ['collapse']}),
    ]
    inlines = [OperationInline]
    
class PartnershipActivityInline(admin.TabularInline):
    model = PartnershipActivity
    extra = 3
    
class PartnershipAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['partner', 'description', 'partnership_type','formal_contract', 'accomplishments','challenges','lessons', 'future_plans']}),
        ('Publication Status', {'fields': ['entry_status'], 'classes': ['collapse']}),
    ]
    list_display = ('partner', 'short_description', 'partnership_type', 'formal_contract', 'entry_status')
    list_filter = ['partnership_type']
    search_fields = ['description', 'partnership_type']
    list_per_page = 20
    inlines = [PartnershipActivityInline]
    
class PoliticalBlockMemberInline(admin.TabularInline):
    model = PoliticalBlockMember
    extra = 3
    
class PoliticalBlockActivityInline(admin.TabularInline):
    model = PoliticalBlockActivity
    extra = 3
    
class PoliticalBlockAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'description', 'goals','accomplishments','challenges','lessons', 'future_plans']}),
        ('Publication Status', {'fields': ['entry_status'], 'classes': ['collapse']}),
    ]
    
    inlines = [PoliticalBlockMemberInline, PoliticalBlockActivityInline]
        
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Partnership, PartnershipAdmin)
admin.site.register(PoliticalBlock, PoliticalBlockAdmin)