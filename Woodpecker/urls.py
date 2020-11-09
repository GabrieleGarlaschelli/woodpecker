from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView

urlpatterns = [
    path('woodworks/', include('woodworks.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^$', RedirectView.as_view(url='woodworks/', permanent=False), name='index'),
]
