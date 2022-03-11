from django.contrib.auth.models import AbstractUser, Group as DjangoGroup
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Customizable User class"""

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")


class Group(DjangoGroup):
    class Meta:
        verbose_name = _("Group")
        verbose_name_plural = _("Groups")
