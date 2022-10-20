"""cooper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

    path('templates/', TemplateView.as_view(template_name ='loginpage.html')),
    
"""
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import include,path
from django.views.generic import TemplateView
from django.conf.urls import url, include
from django.http import HttpResponse
from cooperviews import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('templates/', TemplateView.as_view(template_name ='loginpage.html')),
    path('admin/', admin.site.urls),
    path('', views.principal, name='principal'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('cadastrado/', views.createUser, name='criaruser'),
    path('atualizado/', views.updateAssociado, name='updateassociado'),
    path('ver/', views.view_info, name='verassociados'),#path('ver/', views.PersonListView.as_view(), name='verassociados'),
    path('gerenciar/', views.gerenciar, name='gerenciar'),
    path('gerenciar/associado/', views.checkCpf, name='checkcpf'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.logutView, name = 'logout'),
    path('', views.redirect_view, name='teste'),
    path('', views.principal) 

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]