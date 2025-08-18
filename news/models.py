from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from common.models import BaseModel

User = get_user_model()

class NewsCategory(BaseModel):
    name = models.CharField(max_length=50, verbose_name=_('Kategoriya nomi'))
    slug = models.SlugField(max_length=50, unique=True, verbose_name=_('Slug'))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Yangiliklar kategoriyasi')
        verbose_name_plural = _('Yangiliklar kategoriyalari')

class Tag(BaseModel):
    name = models.CharField(max_length=50, verbose_name=_('Teg nomi'))
    slug = models.SlugField(max_length=50, unique=True, verbose_name=_('Slug'))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Teg')
        verbose_name_plural = _('Teglar')
    
class News(BaseModel):
    title = models.CharField(max_length=255, verbose_name=_('Sarlavha'))
    slug = models.SlugField(max_length=255, unique=True, verbose_name=_('Slug'))
    content = RichTextUploadingField(verbose_name=_('Mazmuni'))

    image = models.ImageField(
        upload_to='media/news/images',
        verbose_name=_('Rasm'),
        help_text=_('Yangilik rasmni yuklang 870x501')
    )

    # 108x74 PNG small image
    image_small = ImageSpecField(
        source='image',
        processors=[ResizeToFill(108, 74)],
        format='PNG',
    )

    # 384x257 PNG medium image
    image_medium = ImageSpecField(
        source='image',
        processors=[ResizeToFill(384, 257)],
        format='PNG',
    )

    is_published = models.BooleanField(default=False, verbose_name=_('Nashr etilgan'))
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name=_('Foydalanuvchi'))
    category = models.ForeignKey(
        NewsCategory,
        on_delete=models.CASCADE,
        related_name='news',
        verbose_name=_('Kategoriya')
    )
    tags = models.ManyToManyField(Tag, verbose_name=_('Teglar'))

    def get_formatted_date(self):
        """Method for formatting dates: MM DD"""
        if self.created:
            return self.created.strftime("%b %d")
        return ""
    
    def get_formatted_year(self):
        """Method for formatting dates: YY"""
        if self.created:
            return self.created.strftime("%Y")
        return ""

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _('Yangilik')
        verbose_name_plural = _('Yangiliklar')