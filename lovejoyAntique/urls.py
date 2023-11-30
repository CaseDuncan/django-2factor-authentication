from django.contrib import admin
from django.urls import path
from antique.views import auth_view, create_evaluation, evaluation, verification_view, register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_view, name='login'),
    path('verify/', verification_view, name='verify'),
    path('register/', register, name='register'),
    path('evaluation/' , evaluation , name='evaluation'),
    path('create_evaluation/' , create_evaluation , name='create_evaluation')
]
