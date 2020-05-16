from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

from . views import (
    InventoryPageView,
)

urlpatterns = [
    path('', InventoryPageView, name='inventory'),
]