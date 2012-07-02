from django.conf.urls.defaults import patterns, include, url
from django.contrib.admin.sites import AdminSite
from django.db import models
from django.views.generic.list import ListView
from pmp_dashboard.views import ReportView, EventsList,\
 EventDetail, CommunicationList, CommunicationDetail, ContactsList, \
 ContactDetail, DistributionsList, DistributionDetail, PartnershipsList, \
 PartnershipDetail, ProposalsList, ProposalDetail
from pmp_events.models import Activity

class ReportSite(AdminSite):

    def get_urls(self):
        urls = super(ReportSite, self).get_urls()
        my_urls = patterns('',
            url(r'reports/$',self.admin_view( ReportView.as_view()), name='report_view' ),
            url(r'communicationlist/', self.admin_view(CommunicationList.as_view()), name='communication_list'),
            url(r'communicationdetail/(?P<pk>\d+)/$', self.admin_view(CommunicationDetail.as_view()), name='communication_view'),
            url(r'contactslist/', self.admin_view(ContactsList.as_view()), name='contacts_list'),
            url(r'contactdetail/(?P<pk>\d+)/$', self.admin_view(ContactDetail.as_view()), name='contact_view'),
            url(r'distributionlist/', self.admin_view(DistributionsList.as_view()), name='distributions_list'),
            url(r'distributiondetail/(?P<pk>\d+)/$', self.admin_view(DistributionDetail.as_view()), name='distribution_view'),
            url(r'eventslist/', self.admin_view(EventsList.as_view()), name='events_list'),
            url(r'eventdetail/(?P<pk>\d+)/$', self.admin_view(EventDetail.as_view()), name='event_view'),
            url(r'partnershipslist/', self.admin_view(PartnershipsList.as_view()), name='partnerships_list'),
            url(r'partnershipdetail/(?P<pk>\d+)/$', self.admin_view(PartnershipDetail.as_view()), name='partnerhsip_view'),
            url(r'proposallist/', self.admin_view(ProposalsList.as_view()), name='proposals_list'),
            url(r'proposaldetail/(?P<pk>\d+)/$', self.admin_view(ProposalDetail.as_view()), name='proposal_view'),
        )

        return my_urls + urls

reports = ReportSite(app_name='pmp_dashboard')

#print reports.urls
#url(r'^admin/', include(my_admin.urls)),
