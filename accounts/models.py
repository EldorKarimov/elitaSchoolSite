from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel

class User(AbstractUser):
    id = models.UUIDField(
        primary_key=True, 
        unique=True, 
        editable=False, 
        default=uuid4,
        verbose_name=_('ID')
    )
    first_name = models.CharField(
        max_length=50, 
        verbose_name=_("Ism")
    )
    last_name = models.CharField(
        max_length=50, 
        verbose_name=_("Familiya")
    )
    patronymic = models.CharField(
        max_length=50, 
        verbose_name=_('Otasining ismi')
    )
    username = models.CharField(
        max_length=50, 
        unique=True, 
        verbose_name=_('Foydalanuvchi nomi')
    )
    email = models.EmailField(
        null=True, 
        blank=True, 
        verbose_name=_('Elektron pochta')
    )

    REQUIRED_FIELDS = ['first_name', 'last_name']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name} {self.patronymic}"
    
    class Meta:
        verbose_name = _('Foydalanuvchi')
        verbose_name_plural = _('Foydalanuvchilar')
   
class Contact(BaseModel):
    full_name = models.CharField(
        max_length=120, 
        verbose_name=_('Toʻliq ism')
    )
    subject = models.CharField(
        max_length=120, 
        verbose_name=_('Mavzu')
    )
    phone_or_email = models.CharField(
        max_length=50, 
        verbose_name=_('Telefon yoki elektron pochta')
    )
    message = models.TextField(
        verbose_name=_('Xabar')
    )

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = _('Aloqa')
        verbose_name_plural = _('Aloqalar')