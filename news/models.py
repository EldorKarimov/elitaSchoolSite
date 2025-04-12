from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField

from common.models import BaseModel

User = get_user_model()

class NewsCategory(BaseModel):
    name = models.CharField(max_length=50, verbose_name=_('name'))
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

class Tag(BaseModel):
    name = models.CharField(max_length=50, verbose_name=_('name'))
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')
    
class News(BaseModel):
    title = models.CharField(max_length=255, verbose_name=_('title'))
    slug = models.SlugField(max_length=255, unique=True)
    content = RichTextUploadingField(verbose_name=_('content'))
    image = models.ImageField(upload_to='media/news/images', verbose_name=_('image'))
    is_published = models.BooleanField(default=False, verbose_name=_('published'))
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name=_('user'))
    category = models.ForeignKey(
        NewsCategory,
        on_delete=models.CASCADE,
        related_name='news',
        verbose_name=_('category')
    )
    tags = models.ManyToManyField(Tag, verbose_name=_('tag'))

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _('new')
        verbose_name_plural = _('news')