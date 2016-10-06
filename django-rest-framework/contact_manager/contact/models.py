from __future__ import unicode_literals

from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    number = models.IntegerField(default=0)
