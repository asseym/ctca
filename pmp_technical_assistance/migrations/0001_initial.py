# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'TechnicalAssistance'
        db.create_table('pmp_technical_assistance_technicalassistance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('activity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pmp_events.Activity'])),
            ('consultant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pmp_contacts.Contact'])),
            ('services', self.gf('django.db.models.fields.TextField')()),
            ('duration', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('objectives', self.gf('django.db.models.fields.TextField')()),
            ('process', self.gf('django.db.models.fields.TextField')()),
            ('audience', self.gf('django.db.models.fields.TextField')()),
            ('outputs', self.gf('django.db.models.fields.TextField')()),
            ('ta_type', self.gf('django.db.models.fields.IntegerField')()),
            ('lessons', self.gf('django.db.models.fields.TextField')()),
            ('evaluation', self.gf('django.db.models.fields.TextField')()),
            ('recommendation', self.gf('django.db.models.fields.TextField')()),
            ('attachments', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('entry_status', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('pmp_technical_assistance', ['TechnicalAssistance'])

        # Adding model 'TechnicalAssistanceFunders'
        db.create_table('pmp_technical_assistance_technicalassistancefunders', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('technical_assistance', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pmp_technical_assistance.TechnicalAssistance'])),
            ('funder', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pmp_proposals.Funder'])),
        ))
        db.send_create_signal('pmp_technical_assistance', ['TechnicalAssistanceFunders'])


    def backwards(self, orm):
        
        # Deleting model 'TechnicalAssistance'
        db.delete_table('pmp_technical_assistance_technicalassistance')

        # Deleting model 'TechnicalAssistanceFunders'
        db.delete_table('pmp_technical_assistance_technicalassistancefunders')


    models = {
        'pmp_contacts.competence': {
            'Meta': {'object_name': 'Competence'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pmp_contacts.Contact']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'qualification': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pmp_contacts.Qualification']"})
        },
        'pmp_contacts.contact': {
            'Meta': {'object_name': 'Contact'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'contact_type': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pmp_countries.Country']"}),
            'entry_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'other_names': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'qualification': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['pmp_contacts.Qualification']", 'through': "orm['pmp_contacts.Competence']", 'symmetrical': 'False'})
        },
        'pmp_contacts.qualification': {
            'Meta': {'object_name': 'Qualification'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'entry_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'pmp_countries.country': {
            'Meta': {'object_name': 'Country'},
            'contact_persons': ('django.db.models.fields.TextField', [], {}),
            'entry_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iso_code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'pmp_events.activity': {
            'Meta': {'object_name': 'Activity'},
            'attachments': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'audience': ('django.db.models.fields.TextField', [], {}),
            'challenges': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'entry_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'event_date': ('django.db.models.fields.DateField', [], {}),
            'event_type': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lessons': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'number_of_participants': ('django.db.models.fields.IntegerField', [], {}),
            'objectives': ('django.db.models.fields.TextField', [], {}),
            'process': ('django.db.models.fields.TextField', [], {}),
            'recommendations': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'results': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user_evaluation': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'pmp_proposals.funder': {
            'Meta': {'object_name': 'Funder'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'entry_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'pmp_technical_assistance.technicalassistance': {
            'Meta': {'object_name': 'TechnicalAssistance'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pmp_events.Activity']"}),
            'attachments': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'audience': ('django.db.models.fields.TextField', [], {}),
            'consultant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pmp_contacts.Contact']"}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'entry_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'evaluation': ('django.db.models.fields.TextField', [], {}),
            'funders': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['pmp_proposals.Funder']", 'through': "orm['pmp_technical_assistance.TechnicalAssistanceFunders']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lessons': ('django.db.models.fields.TextField', [], {}),
            'objectives': ('django.db.models.fields.TextField', [], {}),
            'outputs': ('django.db.models.fields.TextField', [], {}),
            'process': ('django.db.models.fields.TextField', [], {}),
            'recommendation': ('django.db.models.fields.TextField', [], {}),
            'services': ('django.db.models.fields.TextField', [], {}),
            'ta_type': ('django.db.models.fields.IntegerField', [], {})
        },
        'pmp_technical_assistance.technicalassistancefunders': {
            'Meta': {'object_name': 'TechnicalAssistanceFunders'},
            'funder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pmp_proposals.Funder']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'technical_assistance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pmp_technical_assistance.TechnicalAssistance']"})
        }
    }

    complete_apps = ['pmp_technical_assistance']
