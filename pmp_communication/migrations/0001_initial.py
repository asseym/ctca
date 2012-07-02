# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Communication'
        db.create_table('pmp_communication_communication', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('communication_type', self.gf('django.db.models.fields.IntegerField')()),
            ('communication_date', self.gf('django.db.models.fields.DateField')()),
            ('objectives', self.gf('django.db.models.fields.TextField')()),
            ('channel', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('target_audience', self.gf('django.db.models.fields.TextField')()),
            ('recommendations', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('challenges', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('lessons', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('action_points', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('remarks', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('attachments', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('entry_status', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('pmp_communication', ['Communication'])


    def backwards(self, orm):
        
        # Deleting model 'Communication'
        db.delete_table('pmp_communication_communication')


    models = {
        'pmp_communication.communication': {
            'Meta': {'object_name': 'Communication'},
            'action_points': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'attachments': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'challenges': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'channel': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'communication_date': ('django.db.models.fields.DateField', [], {}),
            'communication_type': ('django.db.models.fields.IntegerField', [], {}),
            'entry_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lessons': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'objectives': ('django.db.models.fields.TextField', [], {}),
            'recommendations': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'remarks': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'target_audience': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['pmp_communication']
