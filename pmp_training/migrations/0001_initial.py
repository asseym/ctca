# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'TrainingProgram'
        db.create_table('pmp_training_trainingprogram', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('goals', self.gf('django.db.models.fields.TextField')()),
            ('topics', self.gf('django.db.models.fields.TextField')()),
            ('entry_status', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('pmp_training', ['TrainingProgram'])

        # Adding M2M table for field trainers on 'TrainingProgram'
        db.create_table('pmp_training_trainingprogram_trainers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('trainingprogram', models.ForeignKey(orm['pmp_training.trainingprogram'], null=False)),
            ('contact', models.ForeignKey(orm['pmp_contacts.contact'], null=False))
        ))
        db.create_unique('pmp_training_trainingprogram_trainers', ['trainingprogram_id', 'contact_id'])

        # Adding model 'Training'
        db.create_table('pmp_training_training', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pmp_training.TrainingProgram'])),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('venue', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('training_type', self.gf('django.db.models.fields.IntegerField')()),
            ('female_trainees', self.gf('django.db.models.fields.IntegerField')()),
            ('male_trainees', self.gf('django.db.models.fields.IntegerField')()),
            ('feedback', self.gf('django.db.models.fields.TextField')()),
            ('assessment', self.gf('django.db.models.fields.TextField')()),
            ('follow_up', self.gf('django.db.models.fields.TextField')()),
            ('extra_comments', self.gf('django.db.models.fields.TextField')()),
            ('attachments', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('entry_status', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('pmp_training', ['Training'])


    def backwards(self, orm):
        
        # Deleting model 'TrainingProgram'
        db.delete_table('pmp_training_trainingprogram')

        # Removing M2M table for field trainers on 'TrainingProgram'
        db.delete_table('pmp_training_trainingprogram_trainers')

        # Deleting model 'Training'
        db.delete_table('pmp_training_training')


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
        'pmp_training.training': {
            'Meta': {'object_name': 'Training'},
            'assessment': ('django.db.models.fields.TextField', [], {}),
            'attachments': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pmp_training.TrainingProgram']"}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'entry_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'extra_comments': ('django.db.models.fields.TextField', [], {}),
            'feedback': ('django.db.models.fields.TextField', [], {}),
            'female_trainees': ('django.db.models.fields.IntegerField', [], {}),
            'follow_up': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'male_trainees': ('django.db.models.fields.IntegerField', [], {}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'training_type': ('django.db.models.fields.IntegerField', [], {}),
            'venue': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'pmp_training.trainingprogram': {
            'Meta': {'object_name': 'TrainingProgram'},
            'entry_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'goals': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'topics': ('django.db.models.fields.TextField', [], {}),
            'trainers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['pmp_contacts.Contact']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['pmp_training']
