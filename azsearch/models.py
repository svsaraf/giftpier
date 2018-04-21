from __future__ import unicode_literals

from django.db import models

class Gift(models.Model):
    link = models.URLField(max_length=128)
    image_link = models.URLField(max_length=128)
    name = models.CharField(max_length=128)
    price_desc = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
        return self.name

# Create your models here.
