from django.conf.urls import include, url
from OMRCheck.views import *
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^OMRCheck/', include('OMRCheck.urls')),
    url(r'^admin/', admin.site.urls),
    #url(r'^$', 'django.contrib.auth.views.login'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

