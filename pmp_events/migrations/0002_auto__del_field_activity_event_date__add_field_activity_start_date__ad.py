# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Activity.event_date'
        db.delete_column('pmp_events_activity', 'event_date')

        # Adding field 'Activity.start_date'
        db.add_column('pmp_events_activity', 'start_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 7, 2, 5, 19, 29, 624504)), keep_default=False)

        # Adding field 'Activity.end_date'
        db.add_column('pmp_events_activity', 'end_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 7, 2, 5, 19, 55, 520013)), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Activity.event_date'
        db.add_column('pmp_events_activity', 'event_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 7, 2, 5, 19, 1, 400875)), keep_default=False)

        # Deleting field 'Activity.start_date'
        db.delete_column('pmp_events_activity', 'start_date')

        # Deleting field 'Activity.end_date'
        db.delete_column('pmp_events_activity', 'end_date')


    models = {
        'pmp_events.activity': {
            'Meta': {'object_name': 'Activity'},
            'attachments': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'audience': ('django.db.models.fields.TextField', [], {}),
            'challenges': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'entry_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'user_evaluation': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['pmp_events']
