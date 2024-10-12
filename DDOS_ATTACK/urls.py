"""DDOS_ATTACK URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from data_admins import views as admins

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url('^$',admins.index,name="index"),
    url('user/register', admins.register, name="register"),
    url('user/add_data',admins.add_data,name="add_data"),
    url('user/userpage',admins.userpage,name="userpage"),
    url('user/labeled_data',admins.labeled_data,name="labeled_data"),
    url('user/unlabeled_data',admins.unlabeled_data,name="unlabeled_data"),
    url('user/ddos_analysis',admins.ddos_analysis,name="ddos_analysis"),
    url('user/chart_page/(?P<chart_type>\w+)',admins.chart_page,name="chart_page"),


]
