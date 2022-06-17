from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)

Roles = (('admin', 'admin'), ('creator', 'creator'), ('sale', 'sale'))


class CustomUserManager(BaseUserManager):
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Super user must have is_staff=True')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super user must have is_superuser=True')

        
        if not email:
            raise ValueError('Email field is required')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user



class CustomUser(AbstractBaseUser, PermissionsMixin):
    fullName = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=Roles)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.email

    class Meta:
        ordering = ('created_at', )


class UserActivities(models.Model):
    user = models.ForeignKey(
        CustomUser,  null=True, related_name='user_activities',
        on_delete=models.SET_NULL,
    )
    email = models.EmailField()
    fullName = models.CharField(max_length=255)
    action = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ("-created_at", )
    

    def __str__(self) -> str:
        return f"{self.fullName} {self.action} on {self.created_at.strftime('%Y-%m-%d %H:%M')}"

