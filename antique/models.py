from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import UserManager
import random

# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, phonenumber, password=None, username=''):
        if not phonenumber:
            raise ValueError('Users must have an phonenumber')

        user = self.model(
            phonenumber=phonenumber,
        )
        if not username:
            raise ValueError('superuser must have a username')

        user = self.model(
            username=username,
        )

        user.save(using=self._db)
        return user

    def create_superuser(self, phonenumber, password=None, username=''):
        user = self.model(
            phonenumber=phonenumber
        )
        if not username:
            raise ValueError('superuser must have a username')

        user = self.model(
            username=username,
        )
        user.is_admin = True
        print(password)
        user.set_password(password)
        user.save(using=self._db)
        return user
class CustomUser(AbstractBaseUser):
    phone_number = models.CharField(max_length=12)
    username = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    class Meta:
        db_table = u'customuser'

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