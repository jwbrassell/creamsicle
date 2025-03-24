"""
URL configuration for UniqueName project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from version import VERSION

# Navigation items for the sidebar
navigation_items = [
    {
        'name': 'Dashboard',
        'url_name': 'dashboard',
        'namespace': '',
        'icon': 'fas fa-tachometer-alt'
    },
    {
        'name': 'Admin Panel',
        'url_name': 'admin_panel',
        'namespace': '',
        'icon': 'fas fa-cogs'
    }
]

# Get app name and version for templates
def get_base_context():
    app_name = settings.APP_NAME
    app_name_short = ''.join([word[0].upper() for word in app_name.split()])
    version = settings.PORTAL_VERSION
    
    return {
        'app_name': app_name,
        'app_name_short': app_name_short,
        'version': version,
        'navigation_items': navigation_items,
    }

# Simple view for testing
def home(request):
    return HttpResponse(f"<h1>{settings.APP_NAME} Django App</h1><p>Welcome to the {settings.APP_NAME} Django application.</p>")

# Dashboard view
def dashboard(request):
    context = get_base_context()
    return render(request, 'dashboard.html', context)

# User preferences view
def user_preferences(request):
    context = get_base_context()
    context.update({
        'error_code': '501',
        'error_title': 'Not Implemented',
        'error_message': 'User preferences page is not implemented yet.',
    })
    return render(request, 'error.html', context)

# Admin panel view
def admin_panel(request):
    context = get_base_context()
    context.update({
        'error_code': '501',
        'error_title': 'Not Implemented',
        'error_message': 'Admin panel is not implemented yet.',
    })
    return render(request, 'error.html', context)

# My activity view
def my_activity(request):
    context = get_base_context()
    context.update({
        'error_code': '501',
        'error_title': 'Not Implemented',
        'error_message': 'My activity page is not implemented yet.',
    })
    return render(request, 'error.html', context)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),  # Make dashboard the home page
    path('preferences/', user_preferences, name='user_preferences'),
    path('admin-panel/', admin_panel, name='admin_panel'),
    path('my-activity/', my_activity, name='my_activity'),
]
