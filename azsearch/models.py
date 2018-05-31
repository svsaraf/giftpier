from __future__ import unicode_literals

from django.db import models

class Cart(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    gifts = models.ManyToManyField(Gift)


    def __unicode__(self):
        return str(created)

class Gift(models.Model):
    link = models.URLField(max_length=128)
    image_link = models.URLField(max_length=128)
    name = models.CharField(max_length=128)
    price_desc = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    CATEGORY_CHOICES = (
        ('gender', 'gender'),
        ('age', 'age'),
        ('festival', 'festival'),
    )

    GENDER_CHOICES = (
        ('m', 'male'),
        ('f', 'female'),
    )

    AGE_CHOICES = (
        ('0', '0-5'),
        ('5', '5-8'),
        ('8', '8-11'),
        ('11', '11-12'),
        ('12', '12-15'),
        ('15', '15-18'),
        ('18', '18-22'),
        ('22', '22-30'),
        ('30', '30-40'),
        ('40', '40+'),
    )

    FESTIVAL_CHOICES = (
        ('birthday', 'birthday'),
        ('christmas', 'christmas'),
        ('mother', 'christmas'),
        ('wedding', 'christmas'),
    )

    TAG_CHOICES = GENDER_CHOICES + AGE_CHOICES + FESTIVAL_CHOICES

    gift = models.ForeignKey(Gift)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    tag = models.CharField(max_length=30, choices=TAG_CHOICES)

    def __unicode__(self):
        return self.gift + ' : ' + self.tag

# Create your models here.
