from django.contrib import admin
from django.urls import path
from antique.views import auth_view, verification_view, register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_view, name='login'),
    path('verify/', verification_view, name='verify'),
    path('register/', register, name='register'),
]
