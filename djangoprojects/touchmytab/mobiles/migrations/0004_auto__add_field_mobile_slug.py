# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Mobile.slug'
        db.add_column(u'mobiles_mobile', 'slug',
                      self.gf('django.db.models.fields.SlugField')(max_length=50, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Mobile.slug'
        db.delete_column(u'mobiles_mobile', 'slug')


    models = {
        u'mobiles.mobile': {
            'Meta': {'object_name': 'Mobile'},
            'amazonAmount': ('django.db.models.fields.IntegerField', [], {}),
            'amazonProductUrl': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'flipkartAmount': ('django.db.models.fields.IntegerField', [], {}),
            'flipkartProductUrl': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imageUrl': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'productBrand': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'productDescription': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'snapdealAmount': ('django.db.models.fields.IntegerField', [], {}),
            'snapdealProductUrl': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['mobiles']