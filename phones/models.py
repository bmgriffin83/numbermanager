from django.db import models
from django.utils import timezone

class Phone(models.Model):
	mac = models.CharField(max_length=200)
	make = models.CharField(max_length=200)
	manu = models.CharField(max_length=200)

class Extension(models.Model):
	device = models.ForeignKey('phones.Phone')
	DDI = models.CharField(max_length=200)
	extention = models.CharField(max_length=200)
	site = models.CharField(max_length=200)
	company = models.CharField(max_length=200)
