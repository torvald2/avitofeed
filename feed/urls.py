from django.urls import path
from django.conf.urls import url, include
from django.views.generic import TemplateView

from rest_framework.urlpatterns import format_suffix_patterns
from feed import views

urlpatterns = [
    path('platforms/', views.PlatformList.as_view()),
    path("categories/", views.CategoryList.as_view()),
    path("tables/", views.TableList.as_view()),
    path("cells/", views.CellList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
