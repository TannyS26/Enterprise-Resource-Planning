#import re
#import base64

from io import BytesIO
from django.db.models import Q
from . models import CustomUser, ActivityLog, AccessLog, Role, RoleProfile
from . forms import CustomUserCreationForm, CustomUserChangeForm, RoleForm, RoleProfileForm

from django.views.generic import TemplateView
from django.core.paginator import Paginator
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
#from django.contrib.admin.models import LogEntry
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
#from . forms import RegistrationForm

from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView


from django.contrib.auth.decorators import login_required, user_passes_test

@login_required(login_url='/login/')
def UsersPermissionsPageView(request):
    return render(request, "userspermissions/userspermissions.html")


# User
@user_passes_test(lambda user: user.is_staff and user.is_active, login_url='/')
def user_view(request):
    
    user = CustomUser.objects.all()
    # Show 20 contacts per page
    paginator = Paginator(user, 20)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'userspermissions/user.html', {'page_obj': page_obj})


# Registration
class RegisterView(UserPassesTestMixin, CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('user')
    template_name = 'userspermissions/register.html'

    def test_func(self):
        return self.request.user.is_superuser

# User Update
class UserUpdateView(UserPassesTestMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'userspermissions/update.html'

    def test_func(self):
        return self.request.user.is_superuser


# Role
@user_passes_test(lambda user: user.is_staff and user.is_active, login_url='/')
def role_view(request):
    
    role = Role.objects.all()
    # Show 20 contacts per page
    paginator = Paginator(role, 20)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'userspermissions/role.html', {'page_obj': page_obj})

# Add Role
class AddRole(UserPassesTestMixin, CreateView):
    form_class = RoleForm
    success_url = reverse_lazy('role')
    template_name = 'userspermissions/addrole.html'

    def test_func(self):
        return self.request.user.is_superuser


# Role
@user_passes_test(lambda user: user.is_staff and user.is_active, login_url='/')
def roleprofile_view(request):
    
    roleprofile = RoleProfile.objects.all()
    # Show 20 contacts per page
    paginator = Paginator(roleprofile, 20)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'userspermissions/roleprofile.html', {'page_obj': page_obj})

# Add Role
class AddRoleProfile(UserPassesTestMixin, CreateView):
    form_class = RoleProfileForm
    success_url = reverse_lazy('roleprofile')
    template_name = 'userspermissions/addroleprofile.html'

    def test_func(self):
        return self.request.user.is_superuser



# Activity Logs
@user_passes_test(lambda user: user.is_staff and user.is_active, login_url='/')
def activitylogs(request):
    
    activity_logs = ActivityLog.objects.all()
    # Show 20 contacts per page
    paginator = Paginator(activity_logs, 20)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'userspermissions/activitylogs.html', {'page_obj': page_obj})

# Access Logs
@user_passes_test(lambda user: user.is_staff and user.is_active, login_url='/')
def accesslogs(request):
    
    access_logs = AccessLog.objects.all()
    # Show 20 contacts per page
    paginator = Paginator(access_logs, 20)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'userspermissions/accesslogs.html', {'page_obj': page_obj})