from django.db import models
from django.conf import settings
from django.utils.html import strip_tags
from pmp_countries.models import Country
from pmp_events.models import Activity


ENTRY_STATUS_CHOICES = settings.ENTRY_STATUS_CHOICES

class Partner(models.Model):
    name = models.CharField(max_length=255, help_text=u'Name of Partner e.g School of Public Health, Makerere University etc')
    description = models.TextField(help_text=u'Description and objectives of the organization')
    countries = models.ManyToManyField(Country, help_text=u'Countries working in', through='Operations')
    membership = models.TextField(help_text=u'Membership (where appropriate)', blank=True)
    contact_persons = models.TextField(help_text=u'Contact person(s)', blank=True)
    entry_status = models.BooleanField(choices=ENTRY_STATUS_CHOICES, help_text=u'Approved/Un-approved')
    
    def __unicode__(self):
        return self.name
    
class Operations(models.Model):
    partner = models.ForeignKey(Partner)
    country = models.ForeignKey(Country)
    
    class Meta:
        verbose_name_plural = 'Operations'
        
class Partnership(models.Model):
    """
    CTCA Partnership Tracking Form 
    One form for each organization
    Indicators: 3.2, 3.2.1, 3.2.2, 3.2.3
    """
    PARTNERSHIP_TYPE_CHOICES = (
                        (1, u'short term'),
                        (2, u'project or event related'),
                        (3, u'activities and planning on limited basis'),
                        (4, u'longer term'),
                        (5, u'with contributions of financial or intellectual resources'),
                        (6, u'significant level of integration and sharing of risks'),
                        (7, u'no "end date"'),
                        (8, u'entities dependent on one-another for success')
                        )
    partner = models.ForeignKey(Partner, help_text=u'Name of partner', related_name='partners')
    description = models.TextField(help_text=u'Description of the partnership')
    partnership_type = models.IntegerField(choices=PARTNERSHIP_TYPE_CHOICES, help_text=u'Type of partnership')
    formal_contract = models.BooleanField(help_text='Existence of Formal Contract or MoU', default=True)
    activities = models.ManyToManyField(Activity, help_text=u'List of Activities/Events', through='PartnershipActivity')
    accomplishments = models.TextField(help_text=u'Major accomplishments', blank=True)
    challenges = models.TextField(help_text=u'Challenges', blank=True)
    lessons = models.TextField(help_text=u'Lessons learned', blank=True)
    future_plans = models.TextField(help_text=u'Future plans, next steps', blank=True)
    entry_status = models.BooleanField(choices=ENTRY_STATUS_CHOICES, help_text=u'Approved/Un-approved')

    def short_description(self):
        return strip_tags('%s%s' % (self.description[:150],'...'))
    
    def __unicode__(self):
        return '%s%s' % (self.description[:150],'...')
    
class PartnershipActivity(models.Model):
    partnership = models.ForeignKey(Partnership)
    activity = models.ForeignKey(Activity)
    
    class Meta:
        verbose_name_plural = 'Partnership Activities'
    
class PoliticalBlock(models.Model):
    """
    A PoliciticalBlock is a form of partnership for the following indicators
    Indicators 3.3, 3.3.1
    
    """
    name = models.CharField(max_length=250, help_text=u'Name of Political Block')
    description = models.TextField(help_text=u'Description and Objectives of Block')
    member_countries = models.ManyToManyField(Country, help_text=u'Membership', through='PoliticalBlockMember')
    goals = models.TextField(help_text='Goals/objectives of partnership')
    activities = models.ManyToManyField(Activity, help_text=u'List of Activities/Events', through='PoliticalBlockActivity')
    accomplishments = models.TextField(help_text=u'Major accomplishments', blank=True)
    challenges = models.TextField(help_text=u'Challenges', blank=True)
    lessons = models.TextField(help_text=u'Lessons learned', blank=True)
    future_plans = models.TextField(help_text=u'Future plans, next steps', blank=True)
    entry_status = models.BooleanField(choices=ENTRY_STATUS_CHOICES, help_text=u'Approved/Un-approved')
    
    def __unicode__(self):
        return self.name

class PoliticalBlockActivity(models.Model):
    political_block = models.ForeignKey(PoliticalBlock)
    activity = models.ForeignKey(Activity)
    
    class Meta:
        verbose_name_plural = 'Political Block Activities'
            
class PoliticalBlockMember(models.Model):
    country = models.ForeignKey(Country)
    political_block = models.ForeignKey(PoliticalBlock)
    
    class Meta:
        verbose_name_plural = 'Political Block Members'
