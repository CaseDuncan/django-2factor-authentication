from django.db import models
from django.contrib.auth.models import AbstractBaseUser
import random

# Create your models here.
class CustomUser(AbstractBaseUser):
    phone_number = models.CharField(max_length=12)

class VerificationCode(models.Model):
    code = models.CharField(max_length=5, blank=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def ___str__(self):
        return str(self.code)

    #overide the save method
    def save(self, *args, **kwargs):
        codes = [x for x in range(10)]
        code_items = []

        for x in range(5):
            verification_code = random.choice(codes)
            code_items.append(verification_code)

        verify_code = "".join(str(item) for item in code_items)
        self.code = verify_code
        super().save(*args, **kwargs)