# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Country'
        db.create_table('pmp_countries_country', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('iso_code', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('contact_persons', self.gf('django.db.models.fields.TextField')()),
            ('entry_status', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('pmp_countries', ['Country'])


    def backwards(self, orm):
        
        # Deleting model 'Country'
        db.delete_table('pmp_countries_country')


    models = {
        'pmp_countries.country': {
            'Meta': {'object_name': 'Country'},
            'contact_persons': ('django.db.models.fields.TextField', [], {}),
            'entry_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iso_code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['pmp_countries']
