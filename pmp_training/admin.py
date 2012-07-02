'''
Created on Feb 19, 2012

@author: asseym
'''
from .models import *
from django.contrib import admin
        
class TrainingProgramAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title', 'goals', 'topics', 'trainers']}),
        ('Publication Status', {'fields': ['entry_status'], 'classes': ['collapse']}),
    ]

class TrainingAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['course', 'start_date', 'end_date', 'venue', 'training_type', 'female_trainees', 'male_trainees', 'feedback', 'assessment', 'follow_up', 'extra_comments', 'attachments']}),
        ('Publication Status', {'fields': ['entry_status'], 'classes': ['collapse']}),
    ]
    list_display = ('course', 'start_date', 'end_date', 'venue', 'training_type', 'male_trainees', 'female_trainees', 'attachment', 'entry_status')
    list_filter = ['training_type']
    search_fields = ['course', 'venue']
    list_per_page = 20 
admin.site.register(TrainingProgram, TrainingProgramAdmin)
admin.site.register(Training, TrainingAdmin)