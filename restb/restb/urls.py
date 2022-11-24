
from django.contrib import admin
from django.urls import path, include

urlpatterns = [    
    path('admin/', admin.site.urls),

    path('accounts/', include('allauth.urls')),
    path('api/v1/', include('djoser.urls')),
    path('api/authtoken/', include('djoser.urls.authtoken')),
    path('api/core/', include('core.urls')),
    path('api/users/', include('users.urls')),

]
admin.site.site_header  =  "KashiSoft Administration"  
admin.site.site_title  =  "KashiSoft"
admin.site.index_title  =  "KashiSoft Administration"