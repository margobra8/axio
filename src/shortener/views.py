from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from .models import AxioURL


class AxioRedirectView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        # do something (like analytics ... ...)
        obj = get_object_or_404(AxioURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)

    def post(self, request, shortcode=None, *args, **kwargs):
        return HttpResponse()
