# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Activity'
        db.create_table('pmp_events_activity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('event_type', self.gf('django.db.models.fields.IntegerField')()),
            ('event_date', self.gf('django.db.models.fields.DateField')()),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('objectives', self.gf('django.db.models.fields.TextField')()),
            ('process', self.gf('django.db.models.fields.TextField')()),
            ('audience', self.gf('django.db.models.fields.TextField')()),
            ('number_of_participants', self.gf('django.db.models.fields.IntegerField')()),
            ('results', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('recommendations', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('challenges', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('lessons', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('user_evaluation', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('attachments', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('entry_status', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('pmp_events', ['Activity'])


    def backwards(self, orm):
        
        # Deleting model 'Activity'
        db.delete_table('pmp_events_activity')


    models = {
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
        }
    }

    complete_apps = ['pmp_events']
