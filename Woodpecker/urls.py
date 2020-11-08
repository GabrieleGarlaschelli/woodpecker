from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('woodworks/', include('woodworks.urls')),
    path('admin/', admin.site.urls),
]
