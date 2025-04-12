from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid4)
    first_name = models.CharField(max_length=50, verbose_name=_("first name"))
    last_name = models.CharField(max_length=50, verbose_name=_("last name"))
    patronymic = models.CharField(max_length=50, verbose_name=_('patronymic'))
    username = models.CharField(max_length=50, unique=True, verbose_name=_('username'))
    email = models.EmailField(null=True, blank=True, verbose_name=_('email'))

    REQUIRED_FIELDS = ['first_name', 'last_name']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name} {self.patronymic}"
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
   
class Contact(BaseModel):
    full_name = models.CharField(max_length=120, verbose_name=_('full name'))
    subject = models.CharField(max_length=120, verbose_name=_('subject'))
    phone_or_email = models.CharField(max_length=50, verbose_name=_('phone or email'))
    message = models.TextField(verbose_name=_('message'))

    def __str__(self):
        return self.full_name