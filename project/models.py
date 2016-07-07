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
	phone = models.CharField(max_length=30,null=True)
	address = models.CharField(max_length=500)
	timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)	
	paper = models.CharField(null=True,max_length=50)
	plastic = models.CharField(null=True,max_length=50)
	iron = models.CharField(null=True,max_length=50)
	aluminium = models.CharField(null=True,max_length=50)
	copper = models.CharField(null=True,max_length=50)
	brass = models.CharField(null=True,max_length=50)
	old_batteries = models.CharField(null=True,max_length=50)
	miscellaneous = models.CharField(null=True,max_length=50)
	amount_paid = models.FloatField(null=True)
	request_for = models.CharField(max_length=300)
	confirmation = models.BooleanField(default=False)
	date_of_pickup = models.CharField(max_length=50,null=True)

    # time = models.TimeField(input_formats='%I:%M %p',)
    # time = TimeField(widget=TimeInput(format='%I:%M %p')
	def __unicode__(self): #__str__
		return self.order_id


class RateList(models.Model):
	paper = models.CharField(max_length=50,null=True)
	plastic = models.CharField(max_length=50,null=True)
	copper = models.CharField(max_length=50,null=True)
	aluminium = models.CharField(max_length=50,null=True)
	brass = models.CharField(max_length=50,null=True)
	old_batteries = models.CharField(max_length=50,null=True)
	iron = models.CharField(max_length=50,null=True)
	miscellaneous = models.CharField(max_length=50,null=True)
	def __unicode__(self): #__str__
		return self.paper
