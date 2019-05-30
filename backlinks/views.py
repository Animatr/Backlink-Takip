from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django import template
from bs4 import BeautifulSoup
import requests
# Create your views here.
from .forms import YeniForm
from .models import Backlinks
import re
from requests.exceptions import ConnectionError
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

@login_required
class LinkDelete(DeleteView):
    model = Backlinks
    success_url = "/"
    login_url = "/hesap/login/"

@login_required
class LinkCreate(CreateView):
    model = Backlinks
    form_class = YeniForm
    success_url = "/"
    login_url = "/hesap/login/"

    def form_valid(self, form, **kwargs):
        form.instance.author = self.request.user
        return super().form_valid(form)


@login_required
class BacklinkListView(ListView):
    model = Backlinks
    paginate_by = 25
    login_url = "/hesap/login/"


    def get_queryset(self, *args, **kwargs):
        qs = super(BacklinkListView, self).get_queryset(**kwargs)
        qs = Backlinks.objects.all().order_by('-created_date')
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

@login_required
class BacklinkDetailView(DetailView):
    model = Backlinks
    login_url = "/hesap/login/"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            page = requests.get(self.object.source)
            soup = BeautifulSoup(page.text, 'html.parser')
            backlink = soup.find_all("a", href=lambda href: href and self.object.link in href)
            superlinks = []

            for link in backlink:
                links = link.get('href')
                names = link.contents[0]
                superlinks.append(links)
                superlinks.append(names)
        except ConnectionError as e:    # This is the correct syntax
            superlinks = []
            print(e)
            r = "No response"

        context['results'] = superlinks

        return context
