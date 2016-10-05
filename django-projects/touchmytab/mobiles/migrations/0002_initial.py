# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Mobile'
        db.create_table(u'mobiles_mobile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('productTitle', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('productDescription', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('flipkartProductUrl', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('snapdealProductUrl', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('amazonProductUrl', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('imageUrl', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('flipkartAmount', self.gf('django.db.models.fields.IntegerField')()),
            ('snapdealAmount', self.gf('django.db.models.fields.IntegerField')()),
            ('amazonAmount', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'mobiles', ['Mobile'])


    def backwards(self, orm):
        # Deleting model 'Mobile'
        db.delete_table(u'mobiles_mobile')


    models = {
        u'mobiles.mobile': {
            'Meta': {'object_name': 'Mobile'},
            'amazonAmount': ('django.db.models.fields.IntegerField', [], {}),
            'amazonProductUrl': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'flipkartAmount': ('django.db.models.fields.IntegerField', [], {}),
            'flipkartProductUrl': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imageUrl': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'productDescription': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'productTitle': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'snapdealAmount': ('django.db.models.fields.IntegerField', [], {}),
            'snapdealProductUrl': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['mobiles']