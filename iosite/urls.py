"""iosite URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
import django.contrib.auth.views

urlpatterns = [
		url(r'^admin/', admin.site.urls),
		url(r'^spierdon/', include('spierdon.urls', namespace='spierdon'), name='main'),
		url(r'^$', RedirectView.as_view(url='/spierdon/')),
		url(r'^accounts/login/$', django.contrib.auth.views.login, name="login"),
		url(r'^accounts/logout/$', django.contrib.auth.views.logout, name='logout'),
		url(r'^accounts/password/reset/$', 
			django.contrib.auth.views.password_reset, 
			{'post_reset_redirect' : '/accounts/password/reset/done/'},
			name="password_reset"),
		url(r'^accounts/password/reset/done/$',
			django.contrib.auth.views.password_reset_done),
		url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 
			django.contrib.auth.views.password_reset_confirm, 
			{'post_reset_redirect' : '/accounts/password/done/'}),
		url(r'^accounts/password/done/$', 
			django.contrib.auth.views.password_reset_complete),
		]
