from django.db import models
from django.conf import settings

ENTRY_STATUS_CHOICES = settings.ENTRY_STATUS_CHOICES
FILE_UPLOAD_TO = settings.MEDIA_ROOT

class Activity(models.Model):
    """
    CTCA Events/Activities Tracking Form
    Events = non-training activities, including advocacy meetings, public TC events, conferences, partner meetings, etc.

    """
    EVENT_TYPES = (
                   (1, 'advocacy meeting'),
                   (2, 'public TC event'),
                   (3, 'conference'),
                   (4, 'partner meeting'),
                   )
    name = models.CharField(max_length=255, help_text=u'Name of event e.g conference on impact of tobacco to unborn babies etc')
    description = models.TextField(help_text=u'Description of Event (target audience, brief content etc.)')
    event_type = models.IntegerField(choices=EVENT_TYPES, help_text=u'Non-training activities, including advocacy meetings, public TC events, conferences, partner meetings, etc')
    start_date = models.DateField(help_text=u'Start date of the event')
    end_date = models.DateField(help_text=u'End date of the event')
    location = models.CharField(max_length=100, help_text=u'Location where the event took place')
    objectives = models.TextField(help_text=u'Purpose/objectives of event. Strategic objective output')
    process = models.TextField(help_text=u'Process and methods used in event')
    audience = models.TextField(help_text=u'Who is expected to attend / Who attended')
    number_of_participants = models.IntegerField(help_text=u'How many attended')
    results = models.TextField(help_text=u'Immediate results', blank=True)
    recommendations = models.TextField(help_text=u'Recommendations/next actions', blank=True)
    challenges = models.TextField(help_text=u'Challenges', blank=True)
    lessons = models.TextField(help_text=u'Lessons learned', blank=True)
    user_evaluation = models.TextField(help_text=u'Users evaluation/feedback (including quotes)', blank=True)
    attachments = models.FileField(upload_to=FILE_UPLOAD_TO, help_text=u'Attach all accompanying documents zipped together, e.g training design/agenda, photos, training products, testimonials, etc.', blank=True)
    entry_status = models.BooleanField(choices=ENTRY_STATUS_CHOICES, help_text=u'Approved/Un-approved', default=False)
    
    class Meta:
        verbose_name_plural = 'Events/Activities'
    
    def __unicode__(self):
        return self.name


