from django.contrib import admin
from django.urls import path

from antique.views import auth_view, verification_view, register
from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from antique.views import auth_view, create_evaluation, evaluation, verification_view, register


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_view, name='login'),
    path('verify/', verification_view, name='verify'),
    path('register/', register, name='register'),
    path('password_reset/', PasswordResetView.as_view(template_name='user/password_reset_form.html'),name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password_reset_complete/',PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),name='password_reset_complete'),
    path('evaluation/' , evaluation , name='evaluation'),
    path('create_evaluation/' , create_evaluation , name='create_evaluation')
]
