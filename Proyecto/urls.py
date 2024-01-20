"""Proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import static
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  include('parches.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name='view/VistasPCU/custom_reset_password_form.html',
        email_template_name='view/VistasPCU/custom_reset_password_email.html',
        success_url='/reset_password_send/'), name='password_reset'),

    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(
        template_name='view/VistasPCU/custom_reset_password_done.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='view/VistasPCU/custom_reset_password_confirm.html',
        success_url='/reset_password_complete/'), name='password_reset_confirm'),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='view/VistasPCU/custom_reset_password_complete.html'), name='password_reset_complete'),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
