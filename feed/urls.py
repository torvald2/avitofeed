from django.urls import path
from django.conf.urls import url, include
from django.views.generic import TemplateView

from rest_framework.urlpatterns import format_suffix_patterns
from feed import views

urlpatterns = [
    path('platforms/', views.PlatformList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
