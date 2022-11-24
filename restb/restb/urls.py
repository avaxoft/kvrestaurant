
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve
from django.conf.urls import url

urlpatterns = [    
    path('admin/', admin.site.urls),

    path('accounts/', include('allauth.urls')),
    path('api/v1/', include('djoser.urls')),
    path('api/authtoken/', include('djoser.urls.authtoken')),
    path('api/core/', include('core.urls')),
    path('api/users/', include('users.urls')),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 


]
urlpatterns=urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header  =  "KashiSoft Administration"  
admin.site.site_title  =  "KashiSoft"
admin.site.index_title  =  "KashiSoft Administration"