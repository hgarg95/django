from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import send_mass_mail
from django.views.decorators.csrf import csrf_exempt
from random import randint
# from clickatell.http import Http
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.core import mail
import json
import requests
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.staticfiles.templatetags.staticfiles import static
from math import sin, cos, sqrt, atan2, radians
import demjson
import urllib2
import sys
from django.apps import apps


from .models import User,Orders,RateList


#Create your Views Here.



def home(request):

	# m = request.session.get("name")
	# m1 = request.session.get("name1")
	# context={
	# "m":m,
	# "m1":m1,
	# }
	return render(request, "home.html", {})



@csrf_exempt
def Otp_app(request):
	if request.method == 'POST':
		uphone = request.POST.get("phone")
		uemail = request.POST.get("email")
		uniquekey = request.POST.get("haddhogyibhencho")
		if uniquekey == settings.UNIQUE_KEY:
			query = User.objects.filter(phone=uphone)
			query1 = User.objects.filter(email_id=uemail)
			if(query):
				message = "Phone number already registered"
				return HttpResponse(message)
			elif(query1):
				message = "Email already registered"
				return HttpResponse(message)
			else:
				otp = randint(1000, 9999)
				# a = "jjsdj"+str(uphone)+"hgh"
				# cheapsms_url =  "http://login.cheapsmsbazaar.com/vendorsms/pushsms.aspx?user=myaccountsms&password=garg1995&msisdn=91"+str(uphone)+"&sid=DEMOOO&msg="+str(otp)+"&fl=0&gwid=2"
				# data = urllib2.urlopen(cheapsms_url)
				return HttpResponse(otp)
		else:
			return HttpResponse("Bad Request")

@csrf_exempt
def signup_app(request):

	uemail =  request.POST.get("email")	
	uname =  request.POST.get("name")
	uphone =  request.POST.get("phone")
	upassword =  request.POST.get("password")
	ugender = request.POST.get("gender")
	uniquekey = request.POST.get("haddhogyibhencho")
	if uniquekey == settings.UNIQUE_KEY:	
		p = User(email_id=uemail, password=upassword, name=uname, phone=uphone, gender=ugender)
		p.save()
		return HttpResponse("Successfully registered")

	else:
		return HttpResponse("Bad Request")


@csrf_exempt
def admin_login_app(request):

	uemail = request.POST.get("Id")
	upassword = request.POST.get("Password")
    uniquekey = request.POST.get("haddhogyibhencho")
    if uniquekey == settings.UNIQUE_KEY:
		if uemail != "we3@sykopro" && upassword != "sykokabadi":
			d={}
			dlist=[]
		d["name"]="Invalid Username OR Password"
			dlist.append(d)
			return HttpResponse(json.dumps(dlist))

		else:
			d={}
			dlist=[]
			d['name']="Sykopro"
			dlist.append(d)
			return HttpResponse(json.dumps(dlist))

	else:
		return HttpResponse("Bad Request")
	

@csrf_exempt
def user_login_app(request):

	uemail = request.POST.get("Id")
	upassword = request.POST.get("Password")
    uniquekey = request.POST.get("haddhogyibhencho")
    if uniquekey == settings.UNIQUE_KEY:
		query1 = User.objects.filter(email_id=uemail).filter(password=upassword)
		if not query1:
			d={}
			dlist=[]
			d["name"]="Invalid Username OR Password"
			dlist.append(d)
			return HttpResponse(json.dumps(dlist))

		else:
			d={}
			dlist=[]
			q2 = Orders.objects.filter(email_id=uemail)
			if q2:		
				for instance1 in q2:
					d['flag'] = "success"
					d['order_id'] = instance1.order_id
					d['amount_paid'] = str(instance1.amount_paid)
					d['date_of_pickup'] = instance1.date_of_pickup
					d['paper'] = str(instance1.paper)
					d['plastic'] = str(instance1.plastic)
					d['iron'] = str(instance1.iron)
					d['copper'] = str(instance1.copper)
					d['aluminium'] = str(instance1.aluminium)
					d['brass'] = str(instance1.brass)
					d['old_batteries'] = str(instance1.old_batteries)
					d['miscellaneous'] = str(instance1.miscellaneous)
			else:
				d['flag'] = "failure"
			for instance in query1:
				d['phone']=instance.phone
				d['name']=instance.name
				d['gender']=instance.gender
				dlist.append(d.copy())

			return HttpResponse(json.dumps(dlist))

	else:
		return HttpResponse("Bad Request")


@csrf_exempt
def forgot_password(request):
	email = request.POST.get("email")
    uniquekey = request.POST.get("haddhogyibhencho")
    if uniquekey == settings.UNIQUE_KEY:
		query2 = User.objects.filter(email_id=email)
		if not query2:
			return HttpResponse("Failure")
		else:
			for instance in query2:
				contact = instance.phone
		otp = randint(1000, 9999)
		# a = "jjsdj"+str(uphone)+"hgh"
		cheapsms_url =  "http://login.cheapsmsbazaar.com/vendorsms/pushsms.aspx?user=myaccountsms&password=garg1995&msisdn=918285438096&sid=DEMOOO&msg="+str(otp)+"&fl=0&gwid=2"
		data = urllib2.urlopen(cheapsms_url)
		res = ""+str(contact)+"@"+str(otp)+""
		return HttpResponse(res)

    else:
    	return HttpResponse("Bad Request")


