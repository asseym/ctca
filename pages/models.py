from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=255, help_text='The heading to be displayed on this page')
    content = models.TextField(help_text='The text to be displayed on this page')
    
    class Meta:
        verbose_name = "Content Pages"
        verbose_name_plural = "Content Pages"
    
    def __unicode__(self):
        return '%s' % self.title
