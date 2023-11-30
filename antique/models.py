from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager
import random

# Create your models here.
class CustomUser(AbstractBaseUser):
    phone_number = models.CharField(max_length=12)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    class Meta:
        db_table = 'customuser'

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


class Evaluation(models.Model):
    comment = models.CharField(max_length=1000 , blank=False)
    contact_method = models.CharField(max_length=1000 , blank=False)
    user = models.ForeignKey(CustomUser , on_delete=models.CASCADE, related_name='evaluations')