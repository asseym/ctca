# Create your views here.
from django.db.models.aggregates import Count, Sum
from django.utils.datastructures import SortedDict
from django.db import models
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from pmp_communication.models import Communication
from pmp_contacts.models import Contact
from pmp_distributions.models import Distribution
from pmp_events.models import Activity
from pmp_partnerships.models import Partnership
from pmp_proposals.models import Proposal
from pmp_technical_assistance.models import TechnicalAssistance
from pmp_training.models import Training
import cStringIO as StringIO
import ho.pisa as pisa
#import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from cgi import escape
from django.conf import settings

def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), mimetype='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

def downloadReport(request, **kwargs):
    #Retrieve data or whatever you need
    model = models.get_model(kwargs.get('app_name'), kwargs.get('model_name'))
    report_fields = model._meta.fields + model._meta._many_to_many()
    report = model.objects.get(pk=kwargs.get('pk'))
    return render_to_pdf(
            'admin/reports/report_download.html',
            {
                'pagesize':'A4',
                'report_fields': report_fields,
                'report': report,
            }
        )
    

class ReportView(ListView):
    pass

class EventsList(ListView):
    context_object_name = "reports_list"
    queryset = Activity.objects.exclude(entry_status=False)
    template_name = 'admin/pmp_events/extras/reports_list.html'
    paginated_by = 15

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(EventsList, self).get_context_data(**kwargs)
        queryset = Activity.objects.exclude(entry_status=False).extra(select={'year': "EXTRACT(year FROM event_date)", 'month': "EXTRACT(month from event_date)"}).values('year', 'month').annotate(event_count=Count('pk')).annotate(total_participants=Sum('number_of_participants'))
        context['latest_totals'] = queryset
        return context

class EventDetail(DetailView):
    context_object_name = "report"
    model = Activity
    template_name = 'admin/pmp_events/extras/report_detail.html'

    def get_context_data(self, **kwargs):
        context = super(EventDetail, self).get_context_data(**kwargs)
        model = models.get_model('pmp_events', 'Activity')
        context['report_fields'] = model._meta.fields
        queryset = Activity.objects.exclude(pk=kwargs.get('object').pk).exclude(entry_status=False).order_by('-event_date')[:10]
        context['reports_list'] = queryset
        return context

class CommunicationList(ListView):
    context_object_name = "reports_list"
    queryset = Communication.objects.exclude(entry_status=False)
    template_name = 'admin/pmp_communication/extras/reports_list.html'
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super(CommunicationList, self).get_context_data(**kwargs)
        queryset = Communication.objects.exclude(entry_status=False).extra(select={'year': "EXTRACT(year FROM communication_date)", 'month': "EXTRACT(month from communication_date)"}).values('year', 'month').annotate(communication_count=Count('pk'))
        context['latest_totals'] = queryset
        return context

class CommunicationDetail(DetailView):
    context_object_name = "report"
    model = Communication
    template_name = 'admin/pmp_communication/extras/report_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CommunicationDetail, self).get_context_data(**kwargs)
        model = models.get_model('pmp_communication', 'Communication')
        context['report_fields'] = model._meta.fields
        queryset = Communication.objects.exclude(pk=kwargs.get('object').pk).exclude(entry_status=False).order_by('-communication_date')[:10]
        context['reports_list'] = queryset
        return context

class ContactsList(ListView):
    context_object_name = "reports_list"
    queryset = Contact.objects.exclude(entry_status=False)
    template_name = 'admin/pmp_contacts/extras/reports_list.html'
    paginate_by = 15

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ContactsList, self).get_context_data(**kwargs)
        queryset = Contact.objects.exclude(entry_status=False).values('contact_type').annotate(contact_count=Count('pk'))
        context['latest_totals'] = queryset
        return context

class ContactDetail(DetailView):
    context_object_name = "report"
    model = Contact
    template_name = 'admin/pmp_contacts/extras/report_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ContactDetail, self).get_context_data(**kwargs)
        model = models.get_model('pmp_contacts', 'Contact')
        context['report_fields'] = model._meta.fields
        queryset = Contact.objects.exclude(pk=kwargs.get('object').pk).exclude(entry_status=False)[:10]
        context['reports_list'] = queryset
        return context

class DistributionList(ListView):
    context_object_name = "reports_list"
    queryset = Distribution.objects.exclude(entry_status=False)
    template_name = 'admin/pmp_distributions/extras/reports_list.html'
    paginate_by = 15

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(DistributionList, self).get_context_data(**kwargs)
        queryset = Distribution.objects.exclude(entry_status=False).extra(select={'year': "EXTRACT(year FROM distribution_date)", 'month': "EXTRACT(month from distribution_date)"}).values('year', 'month').annotate(distribution_count=Count('pk'))
        context['latest_totals'] = queryset
        return context

class DistributionDetail(DetailView):
    context_object_name = "report"
    model = Distribution
    template_name = 'admin/pmp_distributions/extras/report_detail.html'

    def get_context_data(self, **kwargs):
        context = super(DistributionDetail, self).get_context_data(**kwargs)
        model = models.get_model('pmp_distributions', 'Distribution')
        context['report_fields'] = model._meta.fields
        queryset = Distribution.objects.exclude(pk=kwargs.get('object').pk).exclude(entry_status=False).order_by('-distribution_date')[:10]
        context['reports_list'] = queryset
        return context

class PartnershipsList(ListView):
    context_object_name = "reports_list"
    queryset = Partnership.objects.exclude(entry_status=False)
    template_name = 'admin/pmp_partnerships/extras/reports_list.html'
    paginate_by = 15

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PartnershipsList, self).get_context_data(**kwargs)
        queryset = Partnership.objects.exclude(entry_status=False).values('partnership_type').annotate(partnership_count=Count('pk'))
        context['latest_totals'] = queryset
        context['partnership_types'] = self.queryset.model.PARTNERSHIP_TYPE_CHOICES
        return context

class PartnershipDetail(DetailView):
    context_object_name = "report"
    model = Partnership
    template_name = 'admin/pmp_partnerships/extras/report_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PartnershipDetail, self).get_context_data(**kwargs)
        model = models.get_model('pmp_partnerships', 'Partnership')
        context['report_fields'] = model._meta.fields
        queryset = Partnership.objects.exclude(pk=kwargs.get('object').pk).exclude(entry_status=False)[:10]
        context['reports_list'] = queryset
        return context
    
class ProposalList(ListView):
    context_object_name = "reports_list"
    queryset = Proposal.objects.exclude(entry_status=False)
    template_name = 'admin/pmp_proposals/extras/reports_list.html'
    paginate_by = 15

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProposalList, self).get_context_data(**kwargs)
        queryset = Proposal.objects.exclude(entry_status=False).extra(select={'year': "EXTRACT(year FROM submission_date)", 'month': "EXTRACT(month from submission_date)"}).values('year', 'month').annotate(submission_count=Count('pk'))
        context['latest_totals'] = queryset
#        context['partnership_types'] = self.queryset.model.PARTNERSHIP_TYPE_CHOICES
        return context

class ProposalDetail(DetailView):
    context_object_name = "report"
    model = Proposal
    template_name = 'admin/pmp_proposals/extras/report_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProposalDetail, self).get_context_data(**kwargs)
        model = models.get_model('pmp_proposals', 'Proposal')
        context['report_fields'] = model._meta.fields
        queryset = Proposal.objects.exclude(pk=kwargs.get('object').pk).order_by('-submission_date').exclude(entry_status=False)[:10]
        context['reports_list'] = queryset
        return context
    
class TechnicalAssistanceList(ListView):
    context_object_name = "reports_list"
    queryset = TechnicalAssistance.objects.exclude(entry_status=False)
    template_name = 'admin/reports/reports_list.html'
    paginate_by = 15

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TechnicalAssistanceList, self).get_context_data(**kwargs)
        queryset = TechnicalAssistance.objects.exclude(entry_status=False).values('ta_type').annotate(ta_type_count=Count('pk'))
        context['total_columns'] = [
                ('ta_type', 'Technical Assistance Type', settings.CHOICE_FIELDS['TechnicalAssistance']), 
                ('ta_type_count', 'Total', False),
        ]
        context['list_columns'] = [
            ('ta_type', 'Technical Assistance Type', False), 
            ('activity', 'Activity', False),
            ('consultant', 'Consultant', False),
            ('duration', 'Duration', False),
            ('funders', 'Funders', False),
            ('attachments', 'Attachments', False),
        ]
        context['view_urls'] = {
            'list_url':'/reports/technicalassistancelist/',
            'detail_url': '/reports/technicalassistancedetail/'
        }
        context['latest_totals'] = queryset
        return context

class TechnicalAssistanceDetail(DetailView):
    context_object_name = "report"
    model = TechnicalAssistance
    template_name = 'admin/reports/report_detail.html'

    def get_context_data(self, **kwargs):
        context = super(TechnicalAssistanceDetail, self).get_context_data(**kwargs)
        model = models.get_model('pmp_technical_assistance', 'TechnicalAssistance')
        context['report_fields'] = model._meta.fields + model._meta._many_to_many()
        queryset = TechnicalAssistance.objects.exclude(pk=kwargs.get('object').pk).exclude(entry_status=False)[:10]
        context['reports_list'] = queryset
        context['list_columns'] = [
            ('ta_type', 'Technical Assistance Type', False), 
            ('activity', 'Activity', False),
            ('consultant', 'Consultant', False),
            ('duration', 'Duration', False),
            ('funders', 'Funders', False),
            ('attachments', 'Attachments', False),
        ]
        context['view_urls'] = {
            'list_url':'/reports/technicalassistancelist/',
            'detail_url': '/reports/technicalassistancedetail/'
        }
        return context
    
class TrainingList(ListView):
    context_object_name = "reports_list"
    queryset = Training.objects.exclude(entry_status=False)
    template_name = 'admin/reports/reports_list.html'
    paginate_by = 15

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TrainingList, self).get_context_data(**kwargs)
        queryset = Training.objects.exclude(entry_status=False).values('training_type').annotate(training_type_count=Count('pk'))
        context['total_columns'] = [
                ('training_type', 'Training Type', settings.CHOICE_FIELDS['Training']), 
                ('training_type_count', 'Total', False),
        ]
        context['list_columns'] = [
            ('course', 'Training Title', False), 
            ('start_date', 'Start Date', False),
            ('end_date', 'End Date', False),
            ('venue', 'Venue', False),
            ('training_type', 'Training Type', False),
            ('male_trainees', 'Male Trainees', False),
            ('female_trainees', 'Female Trainees', False),
            ('attachments', 'Attachments', False),
        ]
        context['view_urls'] = {
            'list_url':'/reports/traininglist/',
            'detail_url': '/reports/trainingdetail/'
        }
        context['latest_totals'] = queryset
        return context

class TrainingDetail(DetailView):
    context_object_name = "report"
    model = Training
    template_name = 'admin/reports/report_detail.html'

    def get_context_data(self, **kwargs):
        context = super(TrainingDetail, self).get_context_data(**kwargs)
        model = models.get_model('pmp_training', 'Training')
        context['report_fields'] = model._meta.fields + model._meta._many_to_many()
        queryset = Training.objects.exclude(pk=kwargs.get('object').pk).exclude(entry_status=False)[:10]
        context['reports_list'] = queryset
        context['list_columns'] = [
            ('course', 'Training Title', False), 
            ('start_date', 'Start Date', False),
            ('end_date', 'End Date', False),
            ('venue', 'Venue', False),
            ('training_type', 'Training Type', False),
            ('male_trainees', 'Male Trainees', False),
            ('female_trainees', 'Female Trainees', False),
            ('attachments', 'Attachments', False),
        ]
        context['view_urls'] = {
            'list_url':'/reports/traininglist/',
            'detail_url': '/reports/trainingdetail/'
        }
        return context