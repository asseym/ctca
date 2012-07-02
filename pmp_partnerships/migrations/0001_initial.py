# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Partner'
        db.create_table('pmp_partnerships_partner', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('membership', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('contact_persons', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('entry_status', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('pmp_partnerships', ['Partner'])

        # Adding model 'Operations'
        db.create_table('pmp_partnerships_operations', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('partner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pmp_partnerships.Partner'])),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pmp_countries.Country'])),
        ))
        db.send_create_signal('pmp_partnerships', ['Operations'])

        # Adding model 'Partnership'
        db.create_table('pmp_partnerships_partnership', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('partner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='partners', to=orm['pmp_partnerships.Partner'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('partnership_type', self.gf('django.db.models.fields.IntegerField')()),
            ('formal_contract', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('accomplishments', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('challenges', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('lessons', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('future_plans', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('entry_status', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('pmp_partnerships', ['Partnership'])

        # Adding model 'PartnershipActivity'
        db.create_table('pmp_partnerships_partnershipactivity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('partnership', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pmp_partnerships.Partnership'])),
            ('activity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pmp_events.Activity'])),
        ))
        db.send_create_signal('pmp_partnerships', ['PartnershipActivity'])

        # Adding model 'PoliticalBlock'
        db.create_table('pmp_partnerships_politicalblock', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('goals', self.gf('django.db.models.fields.TextField')()),
            ('accomplishments', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('challenges', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('lessons', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('future_plans', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('entry_status', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('pmp_partnerships', ['PoliticalBlock'])

        # Adding model 'PoliticalBlockActivity'
        db.create_table('pmp_partnerships_politicalblockactivity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('political_block', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pmp_partnerships.PoliticalBlock'])),
            ('activity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pmp_events.Activity'])),
        ))
        db.send_create_signal('pmp_partnerships', ['PoliticalBlockActivity'])

        # Adding model 'PoliticalBlockMember'
        db.create_table('pmp_partnerships_politicalblockmember', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pmp_countries.Country'])),
            ('political_block', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pmp_partnerships.PoliticalBlock'])),
        ))
        db.send_create_signal('pmp_partnerships', ['PoliticalBlockMember'])


    def backwards(self, orm):
        
        # Deleting model 'Partner'
        db.delete_table('pmp_partnerships_partner')

        # Deleting model 'Operations'
        db.delete_table('pmp_partnerships_operations')

        # Deleting model 'Partnership'
        db.delete_table('pmp_partnerships_partnership')

        # Deleting model 'PartnershipActivity'
        db.delete_table('pmp_partnerships_partnershipactivity')

        # Deleting model 'PoliticalBlock'
        db.delete_table('pmp_partnerships_politicalblock')

        # Deleting model 'PoliticalBlockActivity'
        db.delete_table('pmp_partnerships_politicalblockactivity')

        # Deleting model 'PoliticalBlockMember'
        db.delete_table('pmp_partnerships_politicalblockmember')


    models = {
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
        'pmp_partnerships.operations': {
            'Meta': {'object_name': 'Operations'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pmp_countries.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'partner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pmp_partnerships.Partner']"})
        },
        'pmp_partnerships.partner': {
            'Meta': {'object_name': 'Partner'},
            'contact_persons': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'countries': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['pmp_countries.Country']", 'through': "orm['pmp_partnerships.Operations']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'entry_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'membership': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'pmp_partnerships.partnership': {
            'Meta': {'object_name': 'Partnership'},
            'accomplishments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'activities': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['pmp_events.Activity']", 'through': "orm['pmp_partnerships.PartnershipActivity']", 'symmetrical': 'False'}),
            'challenges': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'entry_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'formal_contract': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'future_plans': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lessons': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'partner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'partners'", 'to': "orm['pmp_partnerships.Partner']"}),
            'partnership_type': ('django.db.models.fields.IntegerField', [], {})
        },
        'pmp_partnerships.partnershipactivity': {
            'Meta': {'object_name': 'PartnershipActivity'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pmp_events.Activity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'partnership': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pmp_partnerships.Partnership']"})
        },
        'pmp_partnerships.politicalblock': {
            'Meta': {'object_name': 'PoliticalBlock'},
            'accomplishments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'activities': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['pmp_events.Activity']", 'through': "orm['pmp_partnerships.PoliticalBlockActivity']", 'symmetrical': 'False'}),
            'challenges': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'entry_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'future_plans': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'goals': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lessons': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'member_countries': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['pmp_countries.Country']", 'through': "orm['pmp_partnerships.PoliticalBlockMember']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'pmp_partnerships.politicalblockactivity': {
            'Meta': {'object_name': 'PoliticalBlockActivity'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pmp_events.Activity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'political_block': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pmp_partnerships.PoliticalBlock']"})
        },
        'pmp_partnerships.politicalblockmember': {
            'Meta': {'object_name': 'PoliticalBlockMember'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pmp_countries.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'political_block': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pmp_partnerships.PoliticalBlock']"})
        }
    }

    complete_apps = ['pmp_partnerships']
