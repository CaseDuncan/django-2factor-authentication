from django.contrib import admin
from antique.models import CustomUser, VerificationCode
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(VerificationCode)