from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin 
from django.conf import settings
import random

# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, *args):
        if not email:
            raise ValueError('User must have an email address')
        
        if not username:
            raise ValueError('User must have an username')

        user = self.model(
            email = self.normalize_email(email),
            username = username
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username, email, password):
         user = self.create_user(
            email = self.normalize_email(email),
            password= password,
            username = username,
         )
         user.is_admin = True
         user.is_active = True
         user.is_staff = True
         user.is_superuser = True
         user.save(using=self.db)
         return user
class CustomUser(AbstractBaseUser, PermissionsMixin ):
    phone_number = models.CharField(max_length=12)
    username = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyUserManager()

    class Meta:
        db_table = 'customuser'

class VerificationCode(models.Model):
    code = models.CharField(max_length=5, blank=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def ___str__(self):
        return str(f"{self.code}")

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
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser , on_delete=models.CASCADE, related_name='evaluations')
    antique_img = models.ImageField(upload_to='evaluation_photos/', null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.comment}'