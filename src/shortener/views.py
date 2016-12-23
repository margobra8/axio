from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import AxioURL
from .forms import SubmitUrlForm


class HomeView(View):
    def get(self, request, *args, **kwargs):
        url_form = SubmitUrlForm()
        context = {"title": "Axio.ga",
                   "form": url_form
                   }
        return render(request, "shortener/home.html", context=context)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data.get("url"))
            new_url = form.cleaned_data.get("url")
            obj, created = AxioURL.objects.get_or_create(url=new_url)

        context = {"form": form}
        return render(request, "shortener/home.html", {})


class AxioRedirectView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        # do something (like analytics ... ...)
        obj = get_object_or_404(AxioURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)

    def post(self, request, shortcode=None, *args, **kwargs):
        return HttpResponse()
