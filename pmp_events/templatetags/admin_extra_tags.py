import calendar
from django import template
from django.contrib.admin.templatetags.admin_list import results, result_headers, result_hidden_fields
from django.conf import settings

def dict(input, property):
    if property in input:
        return input[property]
    else:
        return None

def starts_with(input, property):
    return input.startswith(property)

def remove(input, property):
    x = input.replace(property, '')
    return x.replace('_', ' ').title()

def replace(input, property):
    x = input.replace(property, 'Manage ')
    return x.replace('_', ' ').title()

def has_reports(obj):
    for m in obj['models']:
        if 'Reports' in m['name']:
            return True

def is_report(obj):
    return 'Reports' in obj

def to_int(obj):
    return int(obj)

def month_name(obj):
    return calendar.month_name[obj]

def parse_field_value(obj, attr):
    display_func_name = 'get_'+attr.name+'_display'
    fk_field = attr.name+'_id'
    if display_func_name in dir(obj):
        return obj._get_FIELD_display(attr)
    elif fk_field in dir(obj):
        return obj._meta.get_field(attr.name).rel.to.objects.get(pk=obj.__dict__.get(fk_field))
    else:
        try:
            getattr(obj, attr.name).db_manager
            if getattr(obj, attr.name).all().count() > 0:
                return template.defaultfilters.unordered_list(getattr(obj, attr.name).all())
        except:
            return getattr(obj, attr.name)

def parse_choice_field(input, choices):
    choices_dict = {}
    for k, c in choices:
        choices_dict[k] = c
    return choices_dict.get(input)

def reports_url(obj):
    obj = obj.replace(' Reports', '').lower()
    return '/reports/' + obj.replace(' ','') + 'list'

def is_txt_field(obj):
    return obj.get_internal_type() == 'TextField'

def is_file_field(obj):
    return obj.get_internal_type() == 'FileField'

def url_display(obj):
    if obj.attachments:
        return obj.attachments.url

def file_name(obj):
    return obj.attachments.url.split('/')[-1] if obj.attachments else ''

def app_name(obj):
    return obj._meta.app_label

def model_name(obj):
    return obj.__class__.__name__

def parse_total_values(obj, attr):
    return obj[attr]

def reparse_total_value(obj, choices):
    if choices:
        return parse_choice_field(obj, choices)
    else:
        return obj
    
def parse_list_values(obj, attr):
    CHOICES = settings.CHOICE_FIELDS[model_name(obj)]
    fk_field = attr+'_id'
    if 'get_'+attr+'_display' in dir(obj):
        choice = obj.__dict__.get(attr)
        return parse_choice_field(choice, CHOICES) 
    elif fk_field in dir(obj):
        return obj._meta.get_field(attr).rel.to.objects.get(pk=obj.__dict__.get(fk_field))
    else:
        try:
            getattr(obj, attr).db_manager
            if getattr(obj, attr).all().count() > 0:
                return template.defaultfilters.unordered_list(getattr(obj, attr).all())
        except:
            return getattr(obj, attr)
    
def is_attachment(obj, attr):
    try: 
        getattr(obj, attr).url
        return True
    except:
        return None

def attachment_url(obj, attr):
    return getattr(obj, attr).url

def attachment(obj, attr):
    return getattr(obj, attr).url.split('/')[-1]
    
register = template.Library()

register.filter('dict', dict)
register.filter('starts_with', starts_with)
register.filter('remove', remove)
register.filter('replace', replace)
register.filter('has_reports', has_reports)
register.filter('is_report', is_report)
register.filter('to_int', to_int)
register.filter('month_name', month_name)
register.filter('parse_choice_field', parse_choice_field)
register.filter('parse_field_value', parse_field_value)
register.filter('parse_total_values', parse_total_values)
register.filter('reparse_total_value', reparse_total_value)
register.filter('parse_list_values', parse_list_values)
register.filter('reports_url', reports_url)
register.filter('is_txt_field', is_txt_field)
register.filter('is_file_field', is_file_field)
register.filter('url_display', url_display)
register.filter('file_name', file_name)
register.filter('app_name', app_name)
register.filter('model_name', model_name)
register.filter('is_attachment', is_attachment)
register.filter('attachment_url', attachment_url)
register.filter('attachment', attachment)

