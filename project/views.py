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
import sys
from gcm import *

from django.apps import apps


from .models import User,Orders,RateList
from .forms import ContactForm, CareersForm


#Create your Views Here.



def home(request):

	# m = request.session.get("name")
	# m1 = request.session.get("name1")
	# context={
	# "m":m,
	# "m1":m1,
	# }
	return render(request, "home.html", {})





def contact(request):
	# if request.method == 'POST':
	# 	ustandard = request.POST.get("standard")
		
	# 	p = standard(standard="First")
	# 	p.save()
		

	return render(request, "contact.html", {"form":ContactForm})	



def careers(request):

		
	# 	p = standard(standard="First")
	# 	p.save()
		

	return render(request, "careers.html", {"form":CareersForm})






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
	device_id = request.POST.get("device_id")
	upassword =  request.POST.get("password")
	ugender = request.POST.get("gender")
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
			p = User(email_id=uemail, password=upassword, name=uname, phone=uphone, gender=ugender,device_id=device_id)
			p.save()
			return HttpResponse("Successfully registered")
	else:
		return HttpResponse("Bad Request")



@csrf_exempt
def order_upload(request):
	paper = request.POST.get("paper")
	plastic = request.POST.get("plastic")
	iron = request.POST.get("iron")
	copper = request.POST.get("copper")
	aluminium = request.POST.get("aluminium")
	brass = request.POST.get("brass")
	old_batteries = request.POST.get("old_batteries")
	miscellaneous =request.POST.get("miscellaneous")
	amount = request.POST.get("amount")
	order_id = request.POST.get("order_id")
	uniquekey = request.POST.get("haddhogyibhencho")
	if uniquekey == settings.UNIQUE_KEY:
		q = Orders.objects.filter(order_id=order_id).update(confirmation=True)
		return HttpResponse("Success")
	else:
		return HttpResponse("paper")
	# d={}
	# dlist=[]
	# d["response"]="order"
	# dlist.append(d)
	# return HttpResponse(json.dumps(dlist))




	# return HttpResponse(order)

@csrf_exempt
def order_amount(request):
	order_id = request.POST.get("order_id")
	paper = request.POST.get("paper")
	plastic = request.POST.get("plastic")
	iron = request.POST.get("iron")
	copper = request.POST.get("copper")
	aluminium = request.POST.get("aluminium")
	brass = request.POST.get("brass")
	old_batteries = request.POST.get("old_batteries")
	miscellaneous =request.POST.get("miscellaneous")
	amount = request.POST.get("amount")
	uniquekey = request.POST.get("haddhogyibhencho")
	query = Orders.objects.filter(order_id="GOSYKO4").update(paper="paper", plastic="plastic", iron="iron", aluminium="aluminium", copper="copper", brass="brass", old_batteries="old_batteries", miscellaneous="miscellaneous", amount_paid="amount")
	return HttpResponse(order_id)




def careers_query(request):
	if request.method == 'POST':
		form=CareersForm(request.POST)
		if form.is_valid():
			data=form.cleaned_data
			uname = request.POST.get("Name")
			uemail = request.POST.get("Email")
			ucontact = request.POST.get("Contact")
			uquery = request.POST.get("Post_Your_Query")
			uaddress = request.POST.get("Address")
			ureach = request.POST.get("Reach_Us_As_A")
			# email = settings.DEFAULT_FROM_EMAIL
			# connection = mail.get_connection()
			# connection.open()
			# email1 = mail.EmailMessage('Query For Joining Us', 'This is a Query from ' + str(uname) + '\nMessage: '+str(uquery) + '.\nEmail: '+str(uemail)+'\nContact: ' +str(ucontact)+'\nAddress: '+str(uaddress)+'\nReach Us As A '+str(ureach)+'', email, ['aman1998garg@gmail.com'], connection=connection)
			# email1.send()
			# email2 = mail.EmailMessage('Thanks For Writing To Us!', 'Hi ' +str(uname)+",\nYour Query has been submitted successfully. After screening through the query posted by you, our team will contact you shortly.\n\nSYKOpro is an online platform where people can sell all of their recyclable wastes at the best prices in just one click. Here, at SYKOpro, we try to maintain smooth relations with our clients/employees. Looking forward to Healthy Business in .", email, [str(uemail)])
			# email2.send()
			# connection.close()
			context = {
			"message":"Thanks "+str(uname) +"! Your Query has been submitted. Our team will contact you soon.",
			"form":form,
			}
		else:
			context = {
			"form":form,
			}
	return render(request, "careers.html", context)
	# return HttpResponse(uname)





def contact_query(request):
	if request.method == 'POST':
		form1=ContactForm(request.POST)
		if form1.is_valid():
			data=form1.cleaned_data
			uname = request.POST.get("Name")
			uemail = request.POST.get("Email")
			ucontact = request.POST.get("Contact")
			uquery = request.POST.get("Post_Your_Query")
			# email = settings.DEFAULT_FROM_EMAIL
			# connection = mail.get_connection()
			# connection.open()
			# email1 = mail.EmailMessage('Query For Contact', 'This is a Query from ' + str(uname) + '\n Message: '+str(uquery) + '.\nEmail: '+str(uemail)+'\n Contact: ' +str(ucontact)+'', email, ['aman1998garg@gmail.com'], connection=connection)
			# email1.send()
			# email2 = mail.EmailMessage('Thanks For Writing To Us!', 'Hi ' +str(uname)+",\nYour query has been submitted successfully. Here, we always thrive to provide Best Customer Support to our Users. Our team will contact you soon.", email, [str(uemail)])
			# email2.send()
			# connection.close()		
			context = {
			"message":"Thanks "+str(uname) + " for contacting us. Our team will contact you soon.",
			"form":form1,
			}
		else:
			context = {
			"form":form1,
			}
	return render(request, "contact.html", context)





@csrf_exempt
def admin_login_app(request):

	uemail = request.POST.get("Id")
	upassword = request.POST.get("Password")
	uniquekey = request.POST.get("haddhogyibhencho")
	if uniquekey == settings.UNIQUE_KEY:
		if uemail != "we3@sykopro827682969994.com" or upassword != "humteenomilkarekpapermillkholenge":
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
	uemail = request.POST.get("email")
	uniquekey = request.POST.get("haddhogyibhencho")
	if uniquekey == settings.UNIQUE_KEY:
		query2 = User.objects.filter(email_id=uemail)
		if not query2:
			return HttpResponse("Failure")
		else:
			for instance in query2:
				password = instance.password
		# otp = randint(1000, 9999)
		# a = "jjsdj"+str(uphone)+"hgh"
		# cheapsms_url =  "http://login.cheapsmsbazaar.com/vendorsms/pushsms.aspx?user=myaccountsms&password=garg1995&msisdn=918285438096&sid=DEMOOO&msg="+str(otp)+"&fl=0&gwid=2"
		# data = urllib2.urlopen(cheapsms_url)
		# res = ""+str(contact)+"@"+str(otp)+""
		email = settings.DEFAULT_FROM_EMAIL
		connection = mail.get_connection()
		connection.open()
		# email1 = mail.EmailMessage('Query For Joining Us', 'This is a Query from ' + str(uname) + '\nMessage: '+str(uquery) + '.\nEmail: '+str(uemail)+'\nContact: ' +str(ucontact)+'\nAddress: '+str(uaddress)+'\nReach Us As A '+str(ureach)+'', email, ['aman1998garg@gmail.com'], connection=connection)
		# email1.send()
		email2 = mail.EmailMessage('Hi,\n Your profile information is as follows.\n Email: ' +str(uemail)+"\n Password: "+str(password)+"\n", email, [str(uemail)])
		email2.send()
		return HttpResponse("Success")
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


def send_notify(request):
	# d={}
	# dlist=[]

	# message = { "notification": 
	# {
 #    'message': 'Hello, this is your notification message, We use this variable to store the message text.',
 #    'title': 'This place is for title of the notification',
 #    'tickerText': 'Ticker text for your notifications, Lollipop does not show ticker text by default',
 #    'BigpictureIcon': 'https://cdn4.iconfinder.com/data/icons/iconsimple-logotypes/512/github-512.png',
 #    'largeIcon': 'large_icon_url',
 #    'smallIcon': 'large_icon_url',
	#  "to" : "eB2R2ntrcvI:APA91bEhjH8hyR464L278562t9Sk1hvRrhBC_LCcKrCKaWVWvPEibDAWHbhWJjtlYZlZMz-yTKImb208wCnwTBWXlTOlKAfwUtAtHrv2KqLDTvVYut7UGvdw7YkzAjKVyXvkHfERrcQT",
	# }
	# }
	# requests.post('https://gcm-http.googleapis.com/gcm/send', 
	#   data = json.dumps(message), 
	#   headers = {'Authorization': "AIzaSyBrgfg_u2BTW5wwJzZ3qRJuhAIsN8kmDlI",'Content-Type': 'application/json'})


	gcm = GCM("AIzaSyDOpGF7utwkPGjcv8INWzz8oS7_Q8wflU0")
	data = {'message': 'Cleaning Home Sundays! Sell all of Your Kabaad',
	        'title': 'Sell Your Kabaad This Morning!',
	        'tickerText': 'Ticker text for your notifications, Lollipop does not show ticker text by default',
	        # 'BigpictureIcon': 'https://cdn4.iconfinder.com/data/icons/iconsimple-logotypes/512/github-512.png',
	        'largeIcon': 'https://s3-us-west-2.amazonaws.com/elasticbeanstalk-us-west-2-644902922622/paper.jpg',
	        'smallIcon': '"https://s3-us-west-2.amazonaws.com/elasticbeanstalk-us-west-2-644902922622/App+Icon+192x192.png"'}

	reg_id = ["fVmLB4tyQ2A:APA91bFDibowlCI4Yez9zTIIok7BDwwUCMkT7slzIkBfBTj5ZFG2wSIn5ZeglKY98EbzDSzx2lQ4xVUPiNMujUzKWZAlvMm3cDGwa5cqbGp57iR_5hsiEhoqvID_irpH8AADQuw_a4pt",
	          "dKjBtGnXevY:APA91bF4jpP67U0vT-1qiEDR2TtwLjj88Spjym6tl1XflD22KlvvlHX-uT5Efueg0AfMcQ-kjoP1X45kX48HcgDKRG_By6MbmqZWDyFUEKc8Mty8PXk0rfLz_hFvVq_ZOWPgSOoeuz2-",
	          "daKFirpWvtM:APA91bGMMtU4NT40jAT7funcwFjBMHzr4K5B9KH0akxu87xreHf2xQIrwhPX0KLRV1rdxREKGAxjunM3W7rJLBvEtpp3dxRIZlYX4lQp9JK88ythDU-T7arDC7PXAvj7AorskofY4f-q"]
	# dlist=[]
	# query = User.objects.values_list('device_id',flat=True).distinct() # returns a list of tuples.
	# for instance in query:
	# 	reg_id = instance
	# 	dlist.append(reg_id)
	# # gcm.plaintext_request(registration_id=reg_id,data=data)
	response = json.dumps(gcm.json_request(registration_ids=reg_id, data=data))
	return HttpResponse(response)
		
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
		current_ver = 5 #to be done 3 next tym#
		used_ver = int(ver_code)
		if used_ver<current_ver:
			return HttpResponse("Update@0")
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
def update_rate(request):
	paper = request.POST.get("paper")
	plastic = request.POST.get("plastic")
	iron = request.POST.get("iron")
	copper = request.POST.get("copper")
	aluminium = request.POST.get("aluminium")
	brass = request.POST.get("brass")
	old_batteries = request.POST.get("old_batteries")
	miscellaneous =request.POST.get("miscellaneous")
	uniquekey = request.POST.get("haddhogyibhencho")

	if uniquekey == settings.UNIQUE_KEY:
		p = RateList.objects.all().update(paper=paper,plastic=plastic,iron=iron,copper=copper,aluminium=aluminium,brass=brass,old_batteries=old_batteries,miscellaneous=miscellaneous)
		return HttpResponse ("Success")
	else:
		return HttpResponse("Bad Request")


@csrf_exempt
def orders_admin(request):
	uniquekey = request.POST.get("haddhogyibhencho")
	if uniquekey == settings.UNIQUE_KEY:
		query = Orders.objects.all()
		d={}
		dlist=[]
		for instance in query:
			if not instance.amount_paid:
				d['address'] = instance.address
				d['date'] = instance.date_of_pickup
				d['order_id'] = instance.order_id
				d['confirmation'] = str(instance.confirmation)
				dlist.append(d.copy())
		return HttpResponse(json.dumps(dlist))
	else:
		return HttpResponse("Bad Request")
		
@csrf_exempt
def orders_list(request):
	email=request.POST.get("email")
	uniquekey = request.POST.get("haddhogyibhencho")
	if uniquekey == settings.UNIQUE_KEY:
		query = Orders.objects.filter(email_id=email)
		d={}
		dlist=[]
		for instance in query:
			d['address'] = instance.address
			d['date'] = instance.date_of_pickup
			d['order_id'] = instance.order_id
			if not instance.amount_paid:
				d['status'] = "To be picked up on"
				d['amount'] = "Null"
			else:
				d['status'] = "Picked Up On"
				d['amount'] = instance.amount_paid
			dlist.append(d.copy())
		return HttpResponse(json.dumps(dlist))
	else:
		return HttpResponse("Bad Request")
		
@csrf_exempt
def order_confirm(request):
	order = request.POST.get("order_id")
	uniquekey = request.POST.get("haddhogyibhencho")
	if uniquekey == settings.UNIQUE_KEY:
		query = Orders.objects.filter(order_id=order).update(confirmation=True)
		return HttpResponse("Success")
	else:
		return HttpResponse("Bad Request")
		



@csrf_exempt
def pickup_description(request):
	email = request.POST.get("email")
	order = request.POST.get("order_id")
	uniquekey = request.POST.get("haddhogyibhencho")
	if uniquekey == settings.UNIQUE_KEY:
		query = Orders.objects.filter(email_id=email,order_id=order)
		d={}
		dlist=[]
		for instance in query:
			d['address'] = instance.address
			d['date'] = instance.date_of_pickup
			d['amount'] = instance.amount_paid
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
		email1 = mail.EmailMessage('Pickup Confirmation', 'Hello '+str(name)+'!\nThanks for requesting a SYKO to pickup your scrap. Your requested date is '+str(date_of_pickup)+'. Our SYKO executive will contact you soon.', email, [str(email_id)], connection=connection)
		email1.send()
		email2 = mail.EmailMessage('PickUp Request', 'Request For: '+str(request_for)+'\n Email: '+str(email_id)+'\n Date: '+str(date_of_pickup)+'\n Address: '+str(address)+'\n Contact: '+str(phone)+'', email, ['garg1995speaker@gmail.com'])
		email2.send()
		connection.close()	
		return HttpResponse("Success")
	else:
		return HttpResponse("Bad Request")
		














