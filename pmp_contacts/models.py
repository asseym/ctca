from django.db import models
from django.conf import settings
from django.utils.html import strip_tags
from pmp_countries.models import Country

ENTRY_STATUS_CHOICES = settings.ENTRY_STATUS_CHOICES
FILE_UPLOAD_TO = settings.MEDIA_ROOT

class Qualification(models.Model):
    name = models.CharField(max_length=255, help_text=u'Name of Qualification e.g Computer Skills, Degree, Masters in xxx')
    description = models.TextField(help_text=u'Description of or any other information about the Qualification')
    entry_status = models.BooleanField(choices=ENTRY_STATUS_CHOICES, help_text=u'Approved/Un-approved')
    
    def __unicode__(self):
        return self.name
    
class Contact(models.Model):
    CONTACT_TYPES = (
                       (u'staff', u'CTCA Staff'),
                       (u'consultant',u'Consultant'),
                       (u'focal', u'Focal Person'),
                       (u'partner', u'Partner'),
                       (u'other', u'Other Contact Type')
                       )
    first_name = models.CharField(max_length=30, help_text=u'First name or christian name e.g John', blank=True) 
    other_names = models.CharField(max_length=80, help_text=u'Last/Sir, middle and other names', blank=True)
    organization = models.CharField(max_length=255, help_text=u'Name of the Organization', blank=True)
    position = models.CharField(max_length=60, help_text=u'Position of the personnel, e.g M&E specialist')
    contact_type = models.CharField(max_length=11, choices=CONTACT_TYPES, help_text=u'Personnel type, select staff, consultant etc...')
    address = models.TextField(help_text=u'Address for this contact e.g Street/Location, City/Town, P.O Box Number, Phone, Fax, Email etc')
    qualification = models.ManyToManyField(Qualification, help_text=u'Qualifications/Areas of expertise of the personnel', through='Competence')
    country = models.ForeignKey(Country, help_text=u'Country where the Personnel works')
    entry_status = models.BooleanField(choices=ENTRY_STATUS_CHOICES, help_text=u'Approved/Un-approved')

    def contact_name(self):
        return '%s %s %s' % (self.first_name, self.other_names, self.organization)

    def plain_text_address(self):
        return '%s' % strip_tags(self.address)

    def __unicode__(self):
        return '%s %s %s' % (self.first_name, self.other_names, self.organization)
        
class Competence(models.Model):
    qualification = models.ForeignKey(Qualification)
    contact = models.ForeignKey(Contact)
    
    class Meta:
        verbose_name_plural = 'Competencies'
        
    def __inicode__(self):
        return '%s' % self.qualification
