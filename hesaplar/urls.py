from django.urls import path

from . import views


urlpatterns = [
    path('kayit/', views.SignUp.as_view(), name='signup'),
]
