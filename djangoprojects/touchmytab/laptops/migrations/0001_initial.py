# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Laptop'
        db.create_table(u'laptops_laptop', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('productTitle', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, null=True, blank=True)),
            ('imageUrl', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('flipkartAmount', self.gf('django.db.models.fields.IntegerField')()),
            ('flipkartProductUrl', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('productBrand', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('inStock', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('productColor', self.gf('django.db.models.fields.CharField')(max_length=70)),
        ))
        db.send_create_signal(u'laptops', ['Laptop'])


    def backwards(self, orm):
        # Deleting model 'Laptop'
        db.delete_table(u'laptops_laptop')


    models = {
        u'laptops.laptop': {
            'Meta': {'object_name': 'Laptop'},
            'flipkartAmount': ('django.db.models.fields.IntegerField', [], {}),
            'flipkartProductUrl': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imageUrl': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'inStock': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'productBrand': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'productColor': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'productTitle': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['laptops']