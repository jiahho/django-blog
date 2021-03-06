from django.contrib.auth.models import AbstractUser
from django.urls.base import reverse
from django.db import models


class User(AbstractUser):

    """User Model Definition"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    avatar = models.ImageField(upload_to="avatar", null=True, blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, null=True, blank=True
    )
    bio = models.TextField(default="", blank=True)
    superhost = models.BooleanField(default=False)

    # def get_absolute_url(self):
    #     return reverse("users:profile", kwargs={"pk": self.pk})
