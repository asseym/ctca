# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Grant'
        db.create_table('pmp_proposals_grant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('amount', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('date_obtained', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('duration', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('entry_status', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('pmp_proposals', ['Grant'])

        # Adding model 'Funder'
        db.create_table('pmp_proposals_funder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('entry_status', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('pmp_proposals', ['Funder'])

        # Adding model 'Proposal'
        db.create_table('pmp_proposals_proposal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('submission_date', self.gf('django.db.models.fields.DateField')()),
            ('grant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pmp_proposals.Grant'], blank=True)),
            ('attachments', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('entry_status', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('pmp_proposals', ['Proposal'])

        # Adding model 'ProposalPartners'
        db.create_table('pmp_proposals_proposalpartners', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('partner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pmp_partnerships.Partner'])),
            ('proposal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pmp_proposals.Proposal'])),
        ))
        db.send_create_signal('pmp_proposals', ['ProposalPartners'])

        # Adding model 'ProposalFunders'
        db.create_table('pmp_proposals_proposalfunders', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('funder', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pmp_proposals.Funder'])),
            ('proposal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pmp_proposals.Proposal'])),
        ))
        db.send_create_signal('pmp_proposals', ['ProposalFunders'])


    def backwards(self, orm):
        
        # Deleting model 'Grant'
        db.delete_table('pmp_proposals_grant')

        # Deleting model 'Funder'
        db.delete_table('pmp_proposals_funder')

        # Deleting model 'Proposal'
        db.delete_table('pmp_proposals_proposal')

        # Deleting model 'ProposalPartners'
        db.delete_table('pmp_proposals_proposalpartners')

        # Deleting model 'ProposalFunders'
        db.delete_table('pmp_proposals_proposalfunders')


    models = {
        'pmp_countries.country': {
            'Meta': {'object_name': 'Country'},
            'contact_persons': ('django.db.models.fields.TextField', [], {}),
            'entry_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iso_code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
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
        'pmp_proposals.funder': {
            'Meta': {'object_name': 'Funder'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'entry_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'pmp_proposals.grant': {
            'Meta': {'object_name': 'Grant'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'date_obtained': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'entry_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'pmp_proposals.proposal': {
            'Meta': {'object_name': 'Proposal'},
            'attachments': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'entry_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'grant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pmp_proposals.Grant']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'partners': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['pmp_partnerships.Partner']", 'through': "orm['pmp_proposals.ProposalPartners']", 'symmetrical': 'False'}),
            'submission_date': ('django.db.models.fields.DateField', [], {}),
            'submitted_to': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['pmp_proposals.Funder']", 'through': "orm['pmp_proposals.ProposalFunders']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'pmp_proposals.proposalfunders': {
            'Meta': {'object_name': 'ProposalFunders'},
            'funder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pmp_proposals.Funder']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'proposal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pmp_proposals.Proposal']"})
        },
        'pmp_proposals.proposalpartners': {
            'Meta': {'object_name': 'ProposalPartners'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'partner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pmp_partnerships.Partner']"}),
            'proposal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pmp_proposals.Proposal']"})
        }
    }

    complete_apps = ['pmp_proposals']
