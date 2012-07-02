# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Qualification'
        db.create_table('pmp_contacts_qualification', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('entry_status', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('pmp_contacts', ['Qualification'])

        # Adding model 'Contact'
        db.create_table('pmp_contacts_contact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('other_names', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('organization', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('contact_type', self.gf('django.db.models.fields.CharField')(max_length=11)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pmp_countries.Country'])),
            ('entry_status', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('pmp_contacts', ['Contact'])

        # Adding model 'Competence'
        db.create_table('pmp_contacts_competence', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('qualification', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pmp_contacts.Qualification'])),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pmp_contacts.Contact'])),
        ))
        db.send_create_signal('pmp_contacts', ['Competence'])


    def backwards(self, orm):
        
        # Deleting model 'Qualification'
        db.delete_table('pmp_contacts_qualification')

        # Deleting model 'Contact'
        db.delete_table('pmp_contacts_contact')

        # Deleting model 'Competence'
        db.delete_table('pmp_contacts_competence')


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
        }
    }

    complete_apps = ['pmp_contacts']
