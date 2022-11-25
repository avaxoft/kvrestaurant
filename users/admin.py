from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import Group
from .models import User

class CUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'is_manager', 'is_staffer', 'email')
    list_display_links = ('id', 'username', 'first_name', 'last_name', 'email')
    # list_editable = ('first_name', 'last_name')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        (None, {
            'fields': ( ('username', 'email'), 
                        ('first_name', 'last_name'), 
                        ('is_manager', 'is_staffer'),
                        ('is_active', 'is_staff', 'is_superuser'),
                        ('date_joined', 'last_login'),
                        'password'
            ),
        }),
        # ('Advanced options', {
        #     'classes': ('collapse',),
        #     # 'fields': ('registration_required', 'template_name'),
        # }),
    )
    




admin.site.register(User, CUserAdmin)
# admin.site.unregister(Group)