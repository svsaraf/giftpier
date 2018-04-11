from __future__ import unicode_literals

from django.db import models

class Gift(models.Model):
    link = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    description = models.TextField()

    def __unicode__(self):
        return self.name

# Create your models here.
