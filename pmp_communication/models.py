from django.db import models
from django.conf import settings
from pmp_events.utils import attachment_url, attachment_name

ENTRY_STATUS_CHOICES = settings.ENTRY_STATUS_CHOICES
FILE_UPLOAD_TO = settings.MEDIA_ROOT

class Communication(models.Model):
    EVENT_TYPES = (
        (1, u'Media Event'),
        (2, u'Radio Campaign'),
        (3, u'Press Release'),
        (4, u'TV Campaign')
        )
    title = models.CharField(max_length=255, help_text=u'Title/name of the communication activity')
    communication_type = models.IntegerField(choices=EVENT_TYPES, help_text=u'Communication Type')
    communication_date = models.DateField(help_text=u'Date of the communication event')
    objectives = models.TextField(help_text=u'Objectives of the communication event')
    channel = models.CharField(max_length=255, help_text=u'Channel of communication', blank=True)
    target_audience = models.TextField(help_text=u'The audience which is targeted in this communication event')
    recommendations = models.TextField(help_text=u'Recommendations/next actions', blank=True)
    challenges = models.TextField(help_text=u'Challenges', blank=True)
    lessons = models.TextField(help_text=u'Lessons learned', blank=True)
    action_points = models.TextField(help_text=u'Action Points', blank=True)
    remarks = models.TextField(help_text=u'Other Remarks', blank=True)
    attachments = models.FileField(upload_to=FILE_UPLOAD_TO, help_text=u'Attach all accompanying documents zipped together, e.g agendas, photos, etc.', blank=True)
    entry_status = models.BooleanField(choices=ENTRY_STATUS_CHOICES, help_text=u'Approved/Un-approved')
    
    def attachment(self):
        return attachment_name(self.attachments)
    
    def attachment_url(self):
        return attachment_url(self.attachments)

    class Meta:
        verbose_name_plural = "Communication Events"

    def __unicode__(self):
        return '%s' % self.title
