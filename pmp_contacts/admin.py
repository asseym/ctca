'''
Created on Feb 19, 2012

@author: asseym
'''
from .models import *
from django.contrib import admin
        
class CompetenceInline(admin.TabularInline):
    model = Competence
    extra = 3
    
class ContactAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['first_name', 'other_names', 'organization', 'position', 'contact_type', 'address', 'country']}),
        ('Publication Status', {'fields': ['entry_status'], 'classes': ['collapse']}),
    ]
    list_display = ('contact_name', 'position', 'contact_type', 'plain_text_address', 'country', 'entry_status')
    list_filter = ['contact_type']
    search_fields = ['first_name', 'other_names', 'organization']
    list_per_page = 20
    inlines = [CompetenceInline]
    
class QualificationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'description']}),
        ('Publication Status', {'fields': ['entry_status'], 'classes': ['collapse']}),
    ]
    search_fields = ['name']
    list_per_page = 20
    inlines = [CompetenceInline]

        
admin.site.register(Qualification, QualificationAdmin)
admin.site.register(Contact, ContactAdmin)