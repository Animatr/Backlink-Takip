from django.urls import path,include

from backlinks.views import (
    BacklinkListView,
    BacklinkDetailView,
    LinkCreate,
    LinkDelete,
    )

urlpatterns = [

    path('', BacklinkListView.as_view(), name='home'),
    path('ekle/', LinkCreate.as_view(), name='add'),
    path('detay/<pk>/', BacklinkDetailView.as_view(), name='detail'),
    path('sil/<pk>/', LinkDelete.as_view(), name='delete'),

]
