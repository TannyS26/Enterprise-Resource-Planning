from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

from . views import (
    UsersPermissionsPageView,
    user_view,
    RegisterView,
    UserUpdateView,
    role_view,
    AddRole,
    roleprofile_view,
    AddRoleProfile,
    accesslogs,
    activitylogs,
)

urlpatterns = [
    path('', UsersPermissionsPageView, name='userspermissions'),
    path('user/', user_view, name='user'),
    path('register/', RegisterView.as_view(), name='register'),
    path('role/', role_view, name='role'),
    path('addrole/', AddRole.as_view(), name='addrole'),
    path('roleprofile/', roleprofile_view, name='roleprofile'),
    path('addroleprofile/', AddRoleProfile.as_view(), name='addroleprofile'),
    path('accesslogs/', accesslogs, name='accesslogs'),
    path('activitylogs/', activitylogs, name='activitylogs'),
]