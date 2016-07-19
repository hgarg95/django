"""sykopro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""




from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', 'project.views.home', name='home'),
    url(r'^home/$', 'project.views.home', name='home'),
    url(r'^sitemap\.xml$', TemplateView.as_view(template_name='sitemap.xml', content_type='text/xml')),
    url(r'^robots\.txt$',TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    url(r'^BingSiteAuth\.xml$', TemplateView.as_view(template_name='BingSiteAuth.xml', content_type='text/xml')),
    url(r'^Otp_app/$', 'project.views.Otp_app', name='Otp_app'),
    url(r'^signup_app/$', 'project.views.signup_app', name='signup_app'),
    url(r'^admin_login_app/$', 'project.views.admin_login_app', name='admin_login_app'),    
    url(r'^user_login_app/$', 'project.views.user_login_app', name='user_login_app'),
    url(r'^forgot_password/$', 'project.views.forgot_password', name='forgot_password'),
    url(r'^update_password_user/$', 'project.views.update_password_user', name='update_password_user'),    
    url(r'^update/$', 'project.views.update', name='update'),
    url(r'^update_check/$', 'project.views.update_check', name='update_check'),
    url(r'^Save_address/$', 'project.views.Save_address', name='Save_address'),
    url(r'^address_list/$', 'project.views.address_list', name='address_list'),
    url(r'^pickup/$', 'project.views.pickup', name='pickup'),
    url(r'^pickup_email/$', 'project.views.pickup_email', name='pickup_email'),
    url(r'^orders_list/$', 'project.views.orders_list', name='orders_list'),
    url(r'^rate_list/$', 'project.views.rate_list', name='rate_list'),
    url(r'^pickup_description/$', 'project.views.pickup_description', name='pickup_description'),
    url(r'^contact/$', 'project.views.contact', name='contact'),
    url(r'^careers/$', 'project.views.careers', name='careers'),
    url(r'^send_notify/$', 'project.views.send_notify', name='send_notify'),
    url(r'^careers-query-response/$', 'project.views.careers_query', name='careers_query'),    
    url(r'^update_rate/$', 'project.views.update_rate', name='update_rate'),
    url(r'^orders_admin/$', 'project.views.orders_admin', name='orders_admin'),
    url(r'^order_confirm/$', 'project.views.order_confirm', name='order_confirm'),
    url(r'^order_amount/$', 'project.views.order_amount', name='order_amount'),
    url(r'^order_upload/$', 'project.views.order_upload', name='order_upload'),
    url(r'^contact-query-response/$', 'project.views.contact_query', name='contact_query'),    
    









    url(r'^admin/', admin.site.urls),

    
]
