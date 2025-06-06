from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.root, name='blog_root'),
    path('<int:pk>/', views.detail, name='blog_detail'),
    path('comments/create/', views.create_comment, name='create_comment'),
    path('comments/delete/', views.delete_comment, name='delete_comment'),
]