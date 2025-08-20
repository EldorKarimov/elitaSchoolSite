from django.db import models

from uuid import uuid4
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid4)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Slider(BaseModel):
    title = models.CharField(max_length=255, null=True, verbose_name=_('Sarlavha'))
    short_content = models.TextField(verbose_name=_('Tavsif'), blank=True, null=True)
    button_text = models.CharField(max_length=100, verbose_name=_('Tugma matni'), blank=True, null=True)
    button_link = models.URLField(verbose_name=_('Tugma havolasi'), blank=True, null=True)
    image = models.ImageField(upload_to='media/slider', verbose_name=_('Slider rasmi'))
    
    is_available = models.BooleanField(default=False)

    def __str__(self):
        return str(self.image.name)

class About(BaseModel):
    content = RichTextUploadingField(verbose_name=_('Mazmuni'))

    def __str__(self):
        return f"about-{self.id}"