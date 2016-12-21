"""axio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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

# Importa las views (nuevo método Django 1.10)
from shortener.views import AxioRedirectView, HomeView

# PROHIBIDO HACER:
# from shortener import views ---> se importa el archivo entero de views!
# from otra_app.views import views

# EL ORDEN DE LAS URLs IMPORTA, SE DAN PRIORIDAD A LAS PRIMERAS
urlpatterns = [
    url(r'^manage/', admin.site.urls),
    url(r"^$", HomeView.as_view()),
    url(r"^(?P<shortcode>[\w-]+){6,15}/$", AxioRedirectView.as_view()),

    # PROHIBIDO HACER:
    # url(r"^prueba/$", "shortener.views.axio_redirect_view"),
    # url(r"^prueba/$", views.axio_redirect_view),
]
