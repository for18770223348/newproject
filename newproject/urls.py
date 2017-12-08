"""newproject URL Configuration

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

from app01 import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.login),
    url(r'^logintst/$', views.logintst),
    url(r'^index/$', views.index),
    url(r'^save/$', views.save),
    url(r'^add_question/$', views.add_question),
    url(r'^questionAnire/$', views.questionAnire),

    url(r'^add_questionAnire/$', views.add_questionAnire), #增加问卷  没做
    # url(r'^edit_questionAnire/(\d+)', views.edit_questionAnire), #编辑问卷
    url(r'^edit_questionAnire2/(\d+)/$', views.edit_questionAnire2), #编辑问卷
]
