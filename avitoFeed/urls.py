from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls import url, include

urlpatterns = [
    path('api/v1/', include('feed.urls')),
    url(r'^.*$', TemplateView.as_view(template_name="index.html")),
]