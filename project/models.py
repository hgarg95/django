from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	email_id = models.EmailField(primary_key=True, max_length=50)
	password = models.CharField(max_length=50)
	name = models.CharField(max_length=50)
	phone = models.BigIntegerField(null=True)
	address1 = models.CharField(max_length=500)
	gender = models.CharField(max_length=50, null=True)
	address2 = models.CharField(max_length=500)
	address3 = models.CharField(max_length=500)
	address4 = models.CharField(max_length=500)		

    # time = models.TimeField(input_formats='%I:%M %p',)
    # time = TimeField(widget=TimeInput(format='%I:%M %p')
	def __unicode__(self): #__str__
		return self.email_id

class Orders(models.Model):
	order_id = models.CharField(max_length=50,null=True)	
	count = models.AutoField(primary_key=True)
	email_id = models.EmailField(max_length=50, null=True)
	name = models.CharField(max_length=50)
	phone = models.BigIntegerField(null=True)
	address = models.CharField(max_length=500)
	timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)	
	paper = models.PositiveIntegerField()
	plastic = models.PositiveIntegerField()
	iron = models.PositiveIntegerField()
	aluminium = models.PositiveIntegerField()
	copper = models.PositiveIntegerField()
	brass = models.PositiveIntegerField()
	old_batteries = models.PositiveIntegerField()
	miscellaneous = models.PositiveIntegerField()
	amount_paid = models.FloatField(null=True)
	request_for = models.CharField(max_length=300)
	confirmation = models.BooleanField(default=False)
	date_of_pickup = models.DateTimeField(null=True)

    # time = models.TimeField(input_formats='%I:%M %p',)
    # time = TimeField(widget=TimeInput(format='%I:%M %p')
	def __unicode__(self): #__str__
		return self.order_id


class RateList(models.Model):
	paper = models.FloatField(null=True)
	plastic = models.FloatField(null=True)
	copper = models.FloatField(null=True)
	aluminium = models.FloatField(null=True)
	brass = models.FloatField(null=True)
	old_batteries = models.FloatField(null=True)
	iron = models.FloatField(null=True)
	miscellaneous = models.FloatField(null=True)
	def __unicode__(self): #__str__
		return self.paper
