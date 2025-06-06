from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.root, name='contact_root'),
    path('message/', views.message, name='contact_message'),
]