from django.db import models
from django.conf import settings
from pmp_contacts.models import Contact
from django.utils.html import strip_tags
from pmp_events.utils import attachment_name, attachment_url

ENTRY_STATUS_CHOICES = settings.ENTRY_STATUS_CHOICES
FILE_UPLOAD_TO = settings.MEDIA_ROOT

class TrainingProgram(models.Model):
    title = models.CharField(max_length=255, help_text=u'Course Title/ Name of the course')
    goals = models.TextField(help_text=u'Training Goals/Objectives')
    topics = models.TextField(help_text=u'Training Topics')
    trainers = models.ManyToManyField(Contact, help_text=u'Personnel involved in the conducting the training')
    entry_status = models.BooleanField(choices=ENTRY_STATUS_CHOICES, help_text=u'Approved/Un-approved')
    
    def __unicode__(self):
        return self.title

class Training(models.Model):
    TRAINING_TYPES = settings.CHOICE_FIELDS['Training']
    
    FILE_UPLOAD_TO = settings.MEDIA_ROOT
    course = models.ForeignKey(TrainingProgram, help_text=u'Course Title/ Name of the course')
    start_date = models.DateField(help_text=u'Date the course/training began')
    end_date = models.DateField(help_text=u'Date the course/training was concluded')
    venue = models.CharField(max_length=255, help_text=u'Venue where the course/training was conducted')
    training_type = models.IntegerField(choices=TRAINING_TYPES, help_text=u'Type of the training, national, regional etc')
    female_trainees = models.IntegerField(help_text=u'Number of female trainees that attended the training')
    male_trainees = models.IntegerField(help_text=u'Number of male trainees that attended the training')
    feedback = models.TextField(help_text=u'Participant evaluation and feedback (include quotes when possible)', blank=True)
    assessment = models.TextField(help_text=u'Trainer assessment of training (what went well, what could be improved)', blank=True)
    follow_up = models.TextField(help_text=u'Follow up plans, due date and person(s) responsible', blank=True)
    extra_comments = models.TextField(help_text=u'Additional comments', blank=True)
    attachments = models.FileField(upload_to=FILE_UPLOAD_TO, help_text=u'Attach all accompanying documents zipped together, e.g training design/agenda, photos, training products, testimonials, etc. ', blank=True)
    entry_status = models.BooleanField(choices=ENTRY_STATUS_CHOICES, help_text=u'Approved/Un-approved')
    
    def attachment(self):
        return attachment_name(self.attachments)
    
    def attachment_url(self):
        return attachment_url(self.attachments)

    def __unicode__(self):
        return '%s %s %s' % (self.course, self.venue, self.start_date)
