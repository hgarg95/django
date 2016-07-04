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

urlpatterns = [
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^home/$', 'project.views.home', name='home'),
    url(r'^Otp_app/$', 'project.views.Otp_app', name='Otp_app'),
    url(r'^signup_app/$', 'project.views.signup_app', name='signup_app'),
    url(r'^admin_login_app/$', 'project.views.admin_login_app', name='admin_login_app'),    
    url(r'^user_login_app/$', 'project.views.user_login_app', name='user_login_app'),
    url(r'^forgot_password/$', 'project.views.forgot_password', name='forgot_password'),
    url(r'^update_password_user/$', 'project.views.update_password_user', name='update_password_user'),    








    url(r'^admin/', admin.site.urls),

    
]
