from django.conf.urls.defaults import patterns
from django.contrib import admin
from django.db.models.aggregates import Count
from rpt_reports.models import ActivityReports, CommunicationReports, ContactReports, DistributionReports, PartnershipReports, ProposalReports, TechnicalAssistanceReports, TrainingReports

class ActivityReportsAdmin(admin.ModelAdmin):

#    change_list_template = 'admin/pmp_events/extras/change_list.html'

    def queryset(self, request):
#        return self.model.objects.annotate(number_of_activities=Count('pk')).order_by('-event_date') #values('id','event_date').
#        select={'year': "EXTRACT(year FROM event_date)", 'month': "EXTRACT(month from event_date)"}
#        return self.model.objects.extra(select=select).values('year', 'month', 'id').annotate(number_of_activities=Count('pk')).order_by('-event_date')
        return self.model.objects.order_by('-event_date')

#    def get_activity_reports(self):
#        select={'year': "EXTRACT(year FROM event_date)", 'month': "EXTRACT(month from event_date)"}
#        return self.model.objects.extra(select=select).values('year', 'month').annotate(number_of_activities=Count('pk')).order_by('-event_date')
#
#    def changelist_view(self, request, object_id, extra_context=None):
#        extra_context = extra_context or {}
#        extra_context['activity_reports'] = self.get_activity_reports()
#        return super(ActivityReportsAdmin, self).change_list_view(request, object_id, extra_context=extra_context)

#    fieldsets = [
#        (None,     {'fields':['name','description', 'event_type','event_date','location','objectives','process','audience','number_of_participants','results','recommendations','challenges','lessons','user_evaluation', 'attachments']}),
#        ('Publication Status', {'fields': ['entry_status'], 'classes': ['collapse']}),
#    ]
#
#    list_display = ('name', 'event_type', 'event_date', 'number_of_participants', 'audience')
#    list_filter = ['event_date']
#    search_fields = ['name', 'description']
#    list_per_page = 10

class CommunicationReportsAdmin(admin.ModelAdmin):

    def queryset(self, request):
        return self.model.objects.order_by('-communication_date')

class ContactReportsAdmin(admin.ModelAdmin):
    pass

class DistributionReportsAdmin(admin.ModelAdmin):

    def queryset(self, request):
        return self.model.objects.order_by('-distribution_date')

class PartnershipReportsAdmin(admin.ModelAdmin):
    pass

class ProposalReportsAdmin(admin.ModelAdmin):
    pass

class TechnicalAssistanceReportsAdmin(admin.ModelAdmin):
    pass

class TrainingReportsAdmin(admin.ModelAdmin):
    pass

class ReportsAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super(ReportsAdmin, self).get_urls()
        report_urls = patterns('',
            (r'^reports/$', self.admin_site.admin_view(self.reports_view))
        )
        return report_urls + urls

admin.site.register(ActivityReports, ActivityReportsAdmin)
admin.site.register(CommunicationReports, CommunicationReportsAdmin)
admin.site.register(ContactReports, ContactReportsAdmin)
admin.site.register(DistributionReports, DistributionReportsAdmin)
admin.site.register(PartnershipReports, PartnershipReportsAdmin)
admin.site.register(ProposalReports, ProposalReportsAdmin)
admin.site.register(TechnicalAssistanceReports, TechnicalAssistanceReportsAdmin)
admin.site.register(TrainingReports, TrainingReportsAdmin)