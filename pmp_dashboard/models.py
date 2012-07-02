from django.conf.urls.defaults import patterns, include, url
from django.contrib.admin.sites import AdminSite
from django.db import models
from django.views.generic.list import ListView
from pmp_dashboard.views import *
import inspect
import pmp_dashboard

class ReportSite(AdminSite):
    
    def reports_urlpatterns(self):
        """
        Creates the appropriate URL patterns for reports class-based views
        """
        urlpatterns = patterns('')
        for n, obj in inspect.getmembers(pmp_dashboard.views):
            try:
                if inspect.isclass(obj):
                    name = obj.__name__.lower()
                    if name[-4:] == 'list':    
                        urlpatterns += patterns('', url(r'%s/'%name, self.admin_view(obj.as_view()), name='%s_list'%name))
                    elif name[-4:] == 'tail':
                        urlpatterns += patterns('', url(r'%s/%s'%(name, '(?P<pk>\d+)/'), self.admin_view(obj.as_view()), name='%s_view'%name))
                    else:
                        pass
            except AttributeError:
                pass
        return urlpatterns

    def get_urls(self):
        urls = super(ReportSite, self).get_urls()
        my_urls = patterns('',
            url(r'reports/$',self.admin_view( ReportView.as_view()), name='report_view' ),        
            ('', include(self.reports_urlpatterns())),
            url(r'download/(?P<app_name>[a-zA-Z_]+)/(?P<model_name>[a-zA-Z]+)/(?P<pk>\d+)', downloadReport, name="download"),
        )
        return my_urls + urls

reports = ReportSite(app_name='pmp_dashboard')