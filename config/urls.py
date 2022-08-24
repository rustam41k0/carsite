from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config import settings
from mycarsite.views import *

urlpatterns = [
    path('', include('mycarsite.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)