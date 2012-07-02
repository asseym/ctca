'''
Created on Feb 19, 2012

@author: asseym
'''
from .models import *
from django.contrib import admin

class FunderAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'description']}),
        ('Publication Status', {'fields': ['entry_status'], 'classes': ['collapse']}),
    ]
    
class GrantAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['amount', 'description', 'date_obtained','duration']}),
        ('Publication Status', {'fields': ['entry_status'], 'classes': ['collapse']}),
    ]
    
class ProposalFundersInline(admin.TabularInline):
    model = ProposalFunders
    extra = 3
    
class ProposalPartnersInline(admin.TabularInline):
    model = ProposalPartners
    extra = 3
    
class ProposalAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title', 'description', 'submission_date','grant','attachments']}),
        ('Publication Status', {'fields': ['entry_status'], 'classes': ['collapse']}),
    ]
    list_display = ('title', 'short_description', 'submission_date', 'grant_currency', 'attachment', 'entry_status')
    list_filter = ['submission_date']
    search_fields = ['title', 'description']
    list_per_page = 20
    inlines = [ProposalFundersInline, ProposalPartnersInline]
        
admin.site.register(Funder, FunderAdmin)
admin.site.register(Grant, GrantAdmin)
admin.site.register(Proposal, ProposalAdmin)