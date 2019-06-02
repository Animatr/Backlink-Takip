from django.contrib import admin
from .models import Backlinks


@admin.register(models.Backlinks)
class AuthorAdmin(admin.Backlinks):
  date_hierarchy = 'created_date'
  list_display = ('link','keyword','author')

admin.site.register(Backlinks)
