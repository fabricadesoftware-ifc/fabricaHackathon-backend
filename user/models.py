from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_avaliator = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def save(self, *args, **kwargs):
        student_profile_data = kwargs.pop("student_profile_data", None)
        super().save(*args, **kwargs)
        if student_profile_data:
            StudentProfile.objects.update_or_create(
                user=self, defaults=student_profile_data
            )

    def __str__(self):
        return self.email

    def has_student_profile(self):
        return hasattr(self, "student_profile")


class StudentProfile(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="student_profile"
    )
    whatsapp = models.CharField(max_length=15)
    github = models.URLField()
    portfolio = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    registration = models.CharField(max_length=10)
    class_info = models.ForeignKey(
        "hackathon.ClassInfo", on_delete=models.PROTECT, verbose_name="class", null=True, blank=True
    )
    def __str__(self):
        return f"{self.user.name} - {self.user.id}"
