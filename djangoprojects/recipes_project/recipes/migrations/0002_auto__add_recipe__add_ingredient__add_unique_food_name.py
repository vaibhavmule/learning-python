# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Recipe'
        db.create_table(u'recipes_recipe', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=80)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'recipes', ['Recipe'])

        # Adding model 'Ingredient'
        db.create_table(u'recipes_ingredient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('recipe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipes.Recipe'])),
            ('food', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipes.Food'])),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2)),
            ('measurement', self.gf('django.db.models.fields.SmallIntegerField')()),
        ))
        db.send_create_signal(u'recipes', ['Ingredient'])

        # Adding unique constraint on 'Food', fields ['name']
        db.create_unique(u'recipes_food', ['name'])


    def backwards(self, orm):
        # Removing unique constraint on 'Food', fields ['name']
        db.delete_unique(u'recipes_food', ['name'])

        # Deleting model 'Recipe'
        db.delete_table(u'recipes_recipe')

        # Deleting model 'Ingredient'
        db.delete_table(u'recipes_ingredient')


    models = {
        u'recipes.food': {
            'Meta': {'object_name': 'Food'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        },
        u'recipes.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'food': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipes.Food']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'measurement': ('django.db.models.fields.SmallIntegerField', [], {}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipes.Recipe']"})
        },
        u'recipes.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '80'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        }
    }

    complete_apps = ['recipes']