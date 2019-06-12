from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from backlinktakip.mixins import (
    LoginRequiredMixin,
    )
from django.views.generic import TemplateView
from django import template
import requests
# Create your views here.
from .forms import YeniForm
from .models import Backlinks
import re


class LinkDelete(LoginRequiredMixin,DeleteView):
    model = Backlinks
    success_url = "/"
    login_url = "/hesap/login/"

class LinkCreate(LoginRequiredMixin,CreateView):
    model = Backlinks
    form_class = YeniForm
    success_url = "/"
    login_url = "/hesap/login/"

class BacklinkListView(LoginRequiredMixin,ListView):
    model = Backlinks
    paginate_by = 25
    login_url = "/hesap/login/"

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        qs = super(BacklinkListView, self).get_queryset(**kwargs)
        qs = Backlinks.objects.filter(author=user).order_by('-created_date')
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class BacklinkDetailView(LoginRequiredMixin,DetailView):
    model = Backlinks
    login_url = "/hesap/login/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
