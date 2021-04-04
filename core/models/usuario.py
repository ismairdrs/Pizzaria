import uuid

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField('Email', unique=True,)
    phone_number = models.CharField('Phone', blank=False, max_length=15,)
    first_name = models.CharField(_('first name'), max_length=150, blank=False)
    last_name = models.CharField(_('last name'), max_length=150, blank=False)

    REQUIRED_FIELDS = ['email', 'phone_number', 'first_name', 'last_name', 'password']
