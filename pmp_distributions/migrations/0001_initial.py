# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Material'
        db.create_table('pmp_distributions_material', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('material_type', self.gf('django.db.models.fields.IntegerField')()),
            ('document_language', self.gf('django.db.models.fields.IntegerField')()),
            ('date_developed', self.gf('django.db.models.fields.DateField')()),
            ('objectives', self.gf('django.db.models.fields.TextField')()),
            ('purpose', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('status', self.gf('django.db.models.fields.IntegerField')()),
            ('distributed_to', self.gf('django.db.models.fields.TextField')(max_length=200, blank=True)),
            ('number_distributed', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('reviewed', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('dissemination_plan', self.gf('django.db.models.fields.TextField')()),
            ('users_evaluation', self.gf('django.db.models.fields.TextField')()),
            ('update_plan', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('lessons', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('entry_status', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('pmp_distributions', ['Material'])

        # Adding model 'Distribution'
        db.create_table('pmp_distributions_distribution', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('distribution_date', self.gf('django.db.models.fields.DateField')()),
            ('material', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pmp_distributions.Material'])),
            ('recipient', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('recipient_type', self.gf('django.db.models.fields.IntegerField')()),
            ('entry_status', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('pmp_distributions', ['Distribution'])


    def backwards(self, orm):
        
        # Deleting model 'Material'
        db.delete_table('pmp_distributions_material')

        # Deleting model 'Distribution'
        db.delete_table('pmp_distributions_distribution')


    models = {
        'pmp_distributions.distribution': {
            'Meta': {'object_name': 'Distribution'},
            'distribution_date': ('django.db.models.fields.DateField', [], {}),
            'entry_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'material': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pmp_distributions.Material']"}),
            'recipient': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'recipient_type': ('django.db.models.fields.IntegerField', [], {})
        },
        'pmp_distributions.material': {
            'Meta': {'object_name': 'Material'},
            'date_developed': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'dissemination_plan': ('django.db.models.fields.TextField', [], {}),
            'distributed_to': ('django.db.models.fields.TextField', [], {'max_length': '200', 'blank': 'True'}),
            'document_language': ('django.db.models.fields.IntegerField', [], {}),
            'entry_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lessons': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'material_type': ('django.db.models.fields.IntegerField', [], {}),
            'number_distributed': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'objectives': ('django.db.models.fields.TextField', [], {}),
            'purpose': ('django.db.models.fields.TextField', [], {}),
            'reviewed': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'update_plan': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'users_evaluation': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['pmp_distributions']
