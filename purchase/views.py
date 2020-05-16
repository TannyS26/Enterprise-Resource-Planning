#import re
#import base64

from io import BytesIO
from django.db.models import Q
#from . models import CustomUser, ActivityLog, AccessLog, Role
#from . forms import CustomUserCreationForm, CustomUserChangeForm, RoleForm

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
def PurchasePageView(request):
    return render(request, "purchase/purchase.html")