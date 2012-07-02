'''
Created on May 1, 2012

@author: asseym
'''

#from django.conf import settings
def attachment_url(file):
    return file.url if file else ''

def attachment_name(file):
    return file.url.split('/')[-1] if file else ''