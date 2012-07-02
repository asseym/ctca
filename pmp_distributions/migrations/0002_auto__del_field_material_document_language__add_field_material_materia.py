# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Material.document_language'
        db.delete_column('pmp_distributions_material', 'document_language')

        # Adding field 'Material.material_language'
        db.add_column('pmp_distributions_material', 'material_language', self.gf('django.db.models.fields.IntegerField')(default=1, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Material.document_language'
        db.add_column('pmp_distributions_material', 'document_language', self.gf('django.db.models.fields.IntegerField')(default=1), keep_default=False)

        # Deleting field 'Material.material_language'
        db.delete_column('pmp_distributions_material', 'material_language')


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
            'date_developed': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'dissemination_plan': ('django.db.models.fields.TextField', [], {}),
            'distributed_to': ('django.db.models.fields.TextField', [], {'max_length': '200', 'blank': 'True'}),
            'entry_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lessons': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'material_language': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'material_type': ('django.db.models.fields.IntegerField', [], {}),
            'number_distributed': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'objectives': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'purpose': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'reviewed': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'update_plan': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'users_evaluation': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['pmp_distributions']
