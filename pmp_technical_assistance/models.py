from django.db import models
from django.conf import settings
from pmp_events.models import Activity
from pmp_contacts.models import Contact
from pmp_proposals.models import Funder
from django.utils.html import strip_tags
from pmp_events.utils import attachment_name, attachment_url

ENTRY_STATUS_CHOICES = settings.ENTRY_STATUS_CHOICES
FILE_UPLOAD_TO = settings.MEDIA_ROOT

class TechnicalAssistance(models.Model):
    TA_TYPE_CHOICES = settings.CHOICE_FIELDS['TechnicalAssistance']
    
    activity = models.ForeignKey(Activity, help_text=u'Name of Activity/Event')
    consultant = models.ForeignKey(Contact, help_text=u'Name of Consultant/Expert')
    services = models.TextField(help_text=u'Description of Services Provided (activities, location etc')
    duration = models.CharField(max_length=200, help_text=u'Amount of time provided e.g 3 weeks, 2 months etc')
    objectives = models.TextField(help_text=u'Strategic Objective and Output')
    process = models.TextField(help_text=u'Process/method of TA')
    audience = models.TextField(help_text=u'Target audience')
    outputs = models.TextField(help_text=u'Expected outputs/outcomes')
    ta_type = models.IntegerField(choices=TA_TYPE_CHOICES, verbose_name='Technical Type', help_text=u'Amount of time provided')
    funders = models.ManyToManyField(Funder, help_text=u'Funding for the TA. You may select more than one', through='TechnicalAssistanceFunders')
    lessons = models.TextField(help_text=u'Lessons learned', blank=True)
    evaluation = models.TextField(help_text=u'Evaluation of the Consultant', blank=True)
    recommendation = models.TextField(help_text=u'Recommendation for future work', blank=True)
    attachments = models.FileField(upload_to=FILE_UPLOAD_TO, help_text=u'Attach all accompanying documents zipped together, e.g technical designs/agenda, photos, reports, etc. ', blank=True)
    entry_status = models.BooleanField(choices=ENTRY_STATUS_CHOICES, help_text=u'Approved/Un-approved')
    
    def attachment(self):
        return attachment_name(self.attachments)
    
    def attachment_url(self):
        return attachment_url(self.attachments)
    
    def short_audience(self):
        if self.audience and len(self.audience) > 80:
            return '%s%s' % (strip_tags(self.audience[80]), '...')
        else:
            return '%s' % strip_tags(self.audience)
    
    
    class Meta:
        verbose_name = "Technical Assistance"
        verbose_name_plural = "Technical Assistances"
        
    def __unicode__(self):
        return '%s' % self.activity
    
class TechnicalAssistanceFunders(models.Model):
    technical_assistance = models.ForeignKey(TechnicalAssistance)
    funder = models.ForeignKey(Funder)
