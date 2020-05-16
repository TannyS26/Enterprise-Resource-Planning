from django import forms
from django.db import models
from django.contrib import admin, auth
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from . models import CustomUser, ActivityLog, AccessLog, Role, RoleProfile

from . forms import CustomUserCreationForm, CustomUserChangeForm, RoleForm, RoleProfileForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'date_joined', 'last_login', 'is_staff', 'is_active',)
    list_filter = ('email', 'first_name', 'last_name', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email', 'first_name', 'last_name', 'last_login', 'date_joined')

admin.site.register(CustomUser, CustomUserAdmin)

class RoleAdmin(admin.ModelAdmin):
    form = RoleForm
    model = Role
    
    list_display = ('name', 'status', 'desk_access', 'date_created',)
    readonly_fields = ('date_created',)
    fieldsets = ((
        None, {
            'fields': ('name', 'status', 'desk_access')
        }), (
        'Other Information', {
            'fields': ('date_created',),
            'classes': ('collapse',)
        })
    )
    
    def save_model(self, request, obj, form, change):
        #if not obj.created_by:
            #obj.created_by = request.user.get_full_name
        #obj.last_modified_by = request.user
        obj.save()

admin.site.register(Role, RoleAdmin)


class RoleProfileAdmin(admin.ModelAdmin):
    form = RoleProfileForm
    model = RoleProfile
    
    list_display = ('name', 'date_created',)
    readonly_fields = ('date_created',)
    fieldsets = ((
        None, {
            'fields': ('name', 'roles')
        }), (
        'Other Information', {
            'fields': ('date_created',),
            'classes': ('collapse',)
        })
    )

    formfield_overrides = {
        models.ManyToManyField: {'widget': forms.CheckboxSelectMultiple},
    }
    
    def save_model(self, request, obj, form, change):
        #if not obj.created_by:
            #obj.created_by = request.user.get_full_name
        #obj.last_modified_by = request.user
        obj.save()

admin.site.register(RoleProfile, RoleProfileAdmin)



# ActivityLogs Model Registered.
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('session_key', 'path', 'method', 'ip_address', 'timestamp')
    
    def has_add_permission(self, request, obj=None):
        return False
        
admin.site.register(ActivityLog, ActivityLogAdmin)

# AccessLogs Model Registered.
class AccessLogAdmin(admin.ModelAdmin):
    list_display = ('sys_id', 'session_key', 'path', 'data', 'ip_address', 'referrer', 'timestamp')
    
    def has_add_permission(self, request, obj=None):
        return False

admin.site.register(AccessLog, AccessLogAdmin)

admin.site.unregister(auth.models.Group)