from django.db import models
from django.utils import timezone
from django.conf import settings
from django_userforeignkey.models.fields import UserForeignKey

# Create your models here.

class Backlinks(models.Model):

    link = models.URLField(max_length=100,verbose_name="Link")
    keyword = models.CharField(max_length=100,verbose_name="Anahtar Kelime")
    created_date = models.DateTimeField(default=timezone.now,verbose_name="Eklenme Tarihi")
    end_date = models.DateTimeField(default=timezone.now,verbose_name="Bitiş Tarihi")
    description = models.TextField(null=True,blank=True,verbose_name="Ek Bilgi")
    source = models.URLField(max_length=100,verbose_name="Kaynak")
    author = UserForeignKey(auto_user_add=True, verbose_name="The user that is automatically assigned", related_name="mymodels")

    def __str__(self):
        return self.link

    class Meta:
        verbose_name = 'Backlink'
        verbose_name_plural = 'Backlinkler'
