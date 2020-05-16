from django.db.models import Q
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin

from . forms import LoginForm

class HomePageView(TemplateView):
    template_name = "home.html"


# Login
def login_view(request):
    
    email = ''
    password = ''

    form = LoginForm(request.POST or None)
    if form.is_valid():

        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            context = {'form': form,
                      'error': 'Login Successful'}
            
            return redirect('home')
        else:
            context = {'form': form,
                      'error': 'Invalid Credentials'}
            
            return render(request, 'login.html', context)

    else:
        context = {'form': form}
        return render(request, 'login.html', context)

# Logout
def logout_view(request):
    if request.method == "POST":
        logout(request)
    return render(request, "logout.html")
