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



# def home(request):

# 	# m = request.session.get("name")
# 	# m1 = request.session.get("name1")
# 	# context={
# 	# "m":m,
# 	# "m1":m1,
# 	# }
# 	return render(request, "home.html", {})



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
		if uemail != "we3@sykopro" and upassword != "sykokabadi":
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


@csrf_exempt
def update_password_user(request):
	uemail = request.POST.get("Id")
	upassword = request.POST.get("Password")
	uniquekey = request.POST.get("haddhogyibhencho")
	if uniquekey == settings.UNIQUE_KEY:
		query1 = User.objects.filter(email_id=uemail)
		p = User.objects.filter(email_id=uemail).update(password=upassword)
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
			d['name']=instance.name
			d['phone']=instance.phone
			d['gender']=instance.gender
			dlist.append(d.copy())

		return HttpResponse(json.dumps(dlist))

	else:
		return HttpResponse("Bad Request")
		
@csrf_exempt
def update(request):
	uphone=request.POST.get("Contact")
	uemail=request.POST.get("Email")
	uname=request.POST.get("Name")
	uniquekey = request.POST.get("haddhogyibhencho")
	if uniquekey == settings.UNIQUE_KEY:
		if(uemail == "Same"):
			User.objects.filter(phone=uphone).update(name=uname)
			return HttpResponse("Information Updated Successfully")

		else:

			query1 = User.objects.filter(email_id=uemail)
			if query1:
				return HttpResponse("Email already exists")
			else:

				User.objects.filter(phone=uphone).update(name=uname)
				User.objects.filter(phone=uphone).update(email_id=uemail)
				return HttpResponse("Information Updated Successfully")

	else:
		return HttpResponse("Bad Request")
	
@csrf_exempt
def update_check(request):
	ver_code = request.POST.get("code")
	ver_name = request.POST.get("name")
	uniquekey = request.POST.get("haddhogyibhencho")
	if uniquekey == settings.UNIQUE_KEY:
		current_ver = 2
		used_ver = int(ver_code)
		if used_ver<current_ver:
			return HttpResponse("Update@1")
		else:
			return HttpResponse("No Update")
	else:
		return HttpResponse("Bad Request")



@csrf_exempt
def Save_address(request):
	address = request.POST.get("Address")
	email = request.POST.get("email")
	uniquekey = request.POST.get("haddhogyibhencho")
	if uniquekey == settings.UNIQUE_KEY:
		query = User.objects.filter(email_id=email)
		for instance in query:
			if not str(instance.address1):
				q1 = User.objects.filter(email_id=email).update(address1=address)
				return HttpResponse("Success")
			elif not str(instance.address2):
				q1 = User.objects.filter(email_id=email).update(address2=address)
				return HttpResponse("Success")			
			elif not str(instance.address3):
				q1 = User.objects.filter(email_id=email).update(address3=address)
				return HttpResponse("Success")			
			elif not str(instance.address4):
				q1 = User.objects.filter(email_id=email).update(address4=address)
				return HttpResponse("Success")
			else:
				return HttpResponse("Failure")
	else:
		return HttpResponse("Bad Request")

@csrf_exempt
def rate_list(request):
	uniquekey = request.POST.get("haddhogyibhencho")
	if uniquekey == settings.UNIQUE_KEY:
		q = RateList.objects.all()
		d={}
		dlist=[]	
		for instance in q:
			d['paper'] = instance.paper
			d['plastic'] = instance.plastic
			d['aluminium'] = instance.aluminium
			d['copper'] = instance.copper
			d['brass'] = instance.brass
			d['old_batteries'] = instance.old_batteries
			d['iron'] = instance.iron
			d['miscellaneous'] = instance.miscellaneous
			dlist.append(d.copy())
		return HttpResponse(json.dumps(dlist))
	else:
		return HttpResponse("Bad Request")





@csrf_exempt
def address_list(request):
	email=request.POST.get("email")
	uniquekey = request.POST.get("haddhogyibhencho")
	if uniquekey == settings.UNIQUE_KEY:
		query = User.objects.filter(email_id=email)
		d={}
		dlist=[]
		lst = []
		for instance in query:
			if not str(instance.address1):
				lst.append("Sykopro")
			else:
				lst.append(instance.address1)
			if not str(instance.address2):
				lst.append("Sykopro")
			else:
				lst.append(instance.address2)
			if not str(instance.address3):
				lst.append("Sykopro")
			else:
				lst.append(instance.address3)
			if not str(instance.address4):
				lst.append("Sykopro")
			else:
				lst.append(instance.address4)
		if query:		
			for num in range(1,5):
				for instance in query:
					d['address'] = lst[num-1]
					dlist.append(d.copy())
			return HttpResponse(json.dumps(dlist))
		else:
			return HttpResponse(json.dumps(dlist))
	else:
		return HttpResponse("Bad Request")
		
# @csrf_exempt
# def remove_address(request):
# 	email=request.POST.get("email")
# 	address = request.POST.get("address")
# 	position = request.POST.get("position")
# 	uniquekey = request.POST.get("haddhogyibhencho")
# 	if uniquekey == settings.UNIQUE_KEY:
# 		if int(position) == 1:
# 			User.objects.filter(email_id=email).update(address1="")
# 		if int(position) == 2:
# 			User.objects.filter(email_id=email).update(address2="")
# 		if int(position) == 3:
# 			User.objects.filter(email_id=email).update(address3="")
# 		if int(position) == 4:
# 			User.objects.filter(email_id=email).update(address4="")
# 		return HttpResponse("Successfully Deleted")
# 	else:
# 		return HttpResponse("Bad Request")







@csrf_exempt
def pickup(request):
	email = request.POST.get("email")
	address = request.POST.get("address")
	name = request.POST.get("name")
	phone = request.POST.get("phone")
	request_for = request.POST.get("request_for")
	date_of_pickup = request.POST.get("date_of_pickup")
	uniquekey = request.POST.get("haddhogyibhencho")
	if uniquekey == settings.UNIQUE_KEY:
		c=Orders.objects.count()

		order_id="GOSYKO"+str(c+1)+""

		query = Orders(email_id=email, address=address, name=name, phone=phone, request_for=request_for, order_id=order_id, date_of_pickup=date_of_pickup)
		query.save()

		# url_sms="http://198.24.149.4/API/pushsms.aspx?loginID=9015267601&password=815380&mobile="+str(s_contact)+"&text="+str(text)+"%20"+str(text1)+"%20"+str(text2)+"%20"+str(text3)+"&senderid=DEMOOO&route_id=7&Unicode=0"
		# data1 = urllib2.urlopen(url_sms)	
		# url_sms_2="http://198.24.149.4/API/pushsms.aspx?loginID=9015267601&password=815380&mobile="+str(t_contact)+"&text="+str(text)+"%20"+str(text1)+"%20"+str(text2)+"%20"+str(text3)+"&senderid=DEMOOO&route_id=7&Unicode=0"
		# data2 = urllib2.urlopen(url_sms_2)			

		return HttpResponse("Success")
	else:
		return HttpResponse("Bad Request")
		




@csrf_exempt
def pickup_email(request):
	email_id = request.POST.get("email")
	uniquekey = request.POST.get("haddhogyibhencho")
	address = request.POST.get("address")
	name = request.POST.get("name")
	phone = request.POST.get("phone")
	request_for = request.POST.get("request_for")
	date_of_pickup = request.POST.get("date_of_pickup")
	if uniquekey == settings.UNIQUE_KEY:
		email = settings.DEFAULT_FROM_EMAIL
		connection = mail.get_connection()
		connection.open()
		email1 = mail.EmailMessage('Subject', 'Here is the message', email, ['aman1998garg@gmail.com'], connection=connection)
		email1.send()
		email2 = mail.EmailMessage('Subject here', 'Here is the message', email, ['garg1995speaker@gmail.com'])
		email2.send()
		connection.close()	
		return HttpResponse("Success")
	else:
		return HttpResponse("Bad Request")
		














