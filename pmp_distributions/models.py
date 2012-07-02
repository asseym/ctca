from django.db import models
from django.conf import settings

ENTRY_STATUS_CHOICES = settings.ENTRY_STATUS_CHOICES
FILE_UPLOAD_TO = settings.MEDIA_ROOT

class Material(models.Model):
    """
    CTCA Document or Material Tracking Form
    Tracking of documents and materials related to SO 2, 3, and 4
    """
    MATERIAL_TYPE_CHOICES = (
                             (1, u'training material'),
                             (2, u'toolkit'),
                             (3, u'issue paper'),
                             (4, u'work plan'),
                             (5, u'T-shirts'),
                             (6, u'brochures'),
                             (7, u'newsletter'),
                             (8, u'calendars')
                             )
    STATUS_CHOICES = (
                      (1, u'Translated into French and Portuguese'),
                      (2, u'Posted on CTCA website'),
                      (2, u'Distributed'),
                      (3, u'Reviewed and revised')
                      )
    
    DOCUMENT_LANGUAGE_CHOICES = (
                                 (1, 'English'),
                                 (2, 'French'),
                                 (3, 'Portuguese'),
                                 )
    title = models.CharField(max_length=250, help_text=u'Title of Document or Material')
    material_type = models.IntegerField(choices=MATERIAL_TYPE_CHOICES, help_text=u'Type of material (training material, toolkit, issue paper, work plan, etc.)')
    material_language = models.IntegerField(choices=DOCUMENT_LANGUAGE_CHOICES, help_text=u'Language of material', blank=True)
    date_developed = models.DateField(help_text=u'Date Developed', blank=True)
    objectives = models.TextField(help_text=u'Strategic Objective & Output...', blank=True)
    purpose = models.TextField(help_text=u'Purpose/objectives of document/materials', blank=True)
    description = models.TextField(help_text=u'Description of document/materials (target audience, brief content ect)', blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, help_text=u'Status', blank=True)
    distributed_to = models.TextField(max_length=200, help_text=u'Organization(s) to which the material is distributed to', blank=True)
    number_distributed = models.IntegerField(blank=True)
    reviewed = models.DateField(help_text=u'Date on which the material was reviewed', blank=True)
    dissemination_plan = models.TextField(help_text=u'Plan of Dissemination of document (who and how)')
    users_evaluation = models.TextField(help_text=u"Users' evaluation(include quotes)")
    update_plan = models.TextField(help_text=u'Plans for updating documents/materials', blank=True)
    lessons = models.TextField(help_text=u'Lessons learned (from development, dissemination, use)', blank=True)
    entry_status = models.BooleanField(choices=ENTRY_STATUS_CHOICES, help_text=u'Approved/Un-approved')
    
    def __unicode__(self):
        return self.title

class Distribution(models.Model):
    """
    CTCA Distribution Form
    
    """
    
    ORGANIZATION_TYPE_CHOICES = (
                                 (1, u'Government'),
                                 (2, u'CSO'),
                                 (3, u'Academia'),
                                 (4, u'Media'),
                                 )
    distribution_date = models.DateField(help_text=u'Date of Distribution')
    material = models.ForeignKey(Material, help_text=u'Name or Title of materials')
    recipient = models.CharField(max_length=250, help_text=u'Title and organization of recipient')
    recipient_type = models.IntegerField(choices=ORGANIZATION_TYPE_CHOICES, help_text=u'Categorization of organization')
    entry_status = models.BooleanField(choices=ENTRY_STATUS_CHOICES, help_text=u'Approved/Un-approved')
    
    def __unicode__(self):
        return '%s %s%s' % (self.distribution_date, self.material, '...')
