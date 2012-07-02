from django.db import models
from django.conf import settings
from pmp_partnerships.models import Partner
from django.utils.html import strip_tags
from pmp_events.utils import attachment_url, attachment_name
import locale
locale.setlocale(locale.LC_ALL, '')

ENTRY_STATUS_CHOICES = settings.ENTRY_STATUS_CHOICES
FILE_UPLOAD_TO = settings.MEDIA_ROOT

class Grant(models.Model):
    amount = models.IntegerField(help_text=u'Amount e.g 1000000')
    description = models.TextField(help_text=u'Description of the grant')
    date_obtained = models.DateField(help_text=u'Date the grant was obtained', blank=True)
    duration = models.CharField(max_length=150, help_text=u'Duration of the grant e.g 3 months, 1 year, 10 years etc')
    entry_status = models.BooleanField(choices=ENTRY_STATUS_CHOICES, help_text=u'Approved/Un-approved')
    
    def __unicode__(self):
        return strip_tags('%s - %s%s' % (self.amount, self.description[:80], '...'))
#        return self.amount
    
class Funder(models.Model):
    name = models.CharField(max_length=255, help_text=u'Name of Funder e.g CTCA, WHO etc')
    description = models.TextField(help_text=u'Description of or any other information about the Funder')
    entry_status = models.BooleanField(choices=ENTRY_STATUS_CHOICES, help_text=u'Approved/Un-approved')
    
    def __unicode__(self):
        return self.name
    
class Proposal(models.Model):
    title = models.CharField(max_length=250, help_text=u'Title of Proposal')
    description = models.TextField(help_text=u'Description of or any other information about the Proposal')
    submission_date = models.DateField(help_text=u'Date the proposal was submitted')
    submitted_to = models.ManyToManyField(Funder, help_text=u'Donor to whom the proposal was submitted. You may select more than one', through='ProposalFunders') 
    partners = models.ManyToManyField(Partner, help_text=u'Partner with whom the proposal was submitted', through='ProposalPartners')
    grant = models.ForeignKey(Grant, help_text=u'Grant if already given/known', blank=True)
    attachments = models.FileField(upload_to=FILE_UPLOAD_TO, help_text=u'Attach all accompanying documents zipped together, e.g proposal document. ')
    entry_status = models.BooleanField(choices=ENTRY_STATUS_CHOICES, help_text=u'Approved/Un-approved')
    
    def attachment(self):
        return attachment_name(self.attachments)
    
    def attachment_url(self):
        return attachment_url(self.attachments)
    
    def grant_currency(self):
#        return self.grant.amount
        return strip_tags(locale.currency(self.grant.amount))
    
    def short_description(self):
        if self.description and len(self.description) > 80:
            return '%s%s' % (strip_tags(self.description[80]), '...')
        else:
            return '%s' % strip_tags(self.description)
    
    def __unicode__(self):
        return '%s' % self.title
    
class ProposalPartners(models.Model):
    partner = models.ForeignKey(Partner)
    proposal = models.ForeignKey(Proposal)

class ProposalFunders(models.Model):
    funder = models.ForeignKey(Funder)
    proposal = models.ForeignKey(Proposal)