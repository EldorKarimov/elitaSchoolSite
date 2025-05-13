from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField

from common.models import BaseModel

User = get_user_model()

class Science(BaseModel):
    name = models.CharField(max_length=50, verbose_name=_("name"))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('science')
        verbose_name_plural = _('sciences')
    
class Hobby(BaseModel):
    name = models.CharField(max_length=50, verbose_name=_("name"))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('hobby')
        verbose_name_plural = _('hobbies')
    
class Teacher(BaseModel):
    DEGREE_CHOICES = [
        ('BACHELOR', _("Bachelor")),
        ('MASTER', _("Master")),
        ('PHD', _("PhD")),
        ('DSC', _("Doctor of Science (DSc)")),  # Doctor of Sciences
        ('PROFESSOR', _("Professor")),
        ('ASSOCIATE_PROF', _("Associate Professor")),
        ('RESEARCHER', _("Senior Researcher")),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('user'))
    image = models.ImageField(upload_to='media/accounts/teacher/', verbose_name=_('image'))
    experience = models.CharField(max_length=255, verbose_name=_('experience'))
    phone = models.CharField(max_length=13, verbose_name=_('phone'))
    about = RichTextUploadingField(verbose_name=_('about teacher'))
    hobbies = models.ManyToManyField(Hobby, verbose_name=_('hobbies'))
    sciences = models.ManyToManyField(Science, verbose_name=_('sciences'))
    degree_type = models.CharField(max_length=15, choices=DEGREE_CHOICES, default="BACHELOR")

    def __str__(self):
        return str(self.user.get_full_name())

    class Meta:
        verbose_name = _('teacher')
        verbose_name_plural = _('teachers')

class Skill(BaseModel):
    name = models.CharField(max_length=50, verbose_name=_('name'))
    percent = models.PositiveIntegerField(verbose_name=_('percent'))
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name=_('teacher'))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('skill')
        verbose_name_plural = _('skills')

class TeacherSchedule(BaseModel):
    teacher = models.ForeignKey(Teacher, related_name='teacher', on_delete=models.CASCADE, verbose_name=_('teacher'))
    weekday = models.CharField(max_length=50, verbose_name=_('weekday'))
    time_from = models.TimeField(verbose_name=_('time from'))
    time_to = models.TimeField(verbose_name=_('time to'))

    def __str__(self):
        return str(self.teacher.user.get_full_name)
    
    class Meta:
        verbose_name = _('teacher schedule')
        verbose_name_plural = _('teacher schedules')
 

class SchoolClass(BaseModel):
    class TransportationChoices(models.TextChoices):
        AVAILABLE = 'AVAILABLE', _('Available')
        UNAVAILABLE = 'UNAVAILABLE', _('Unavailable')
    name = models.CharField(max_length=50, verbose_name=_('name'))
    slug = models.SlugField(max_length=50, unique=True, verbose_name=_('slug'))
    start_date = models.DateField(verbose_name=_('start date'))
    size = models.PositiveIntegerField(default=20, verbose_name=_('size'))
    transportation = models.CharField(max_length=11, choices=TransportationChoices.choices)
    food = models.CharField(max_length=50, verbose_name=_('food'))
    description = RichTextUploadingField(verbose_name=_('description'))
    head_teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        related_name='teacher_classes',
        verbose_name=_('head teacher'),
    )
    teachers = models.ManyToManyField(Teacher, verbose_name=_('teachers'))
    lesson_start = models.TimeField(default='08:30', verbose_name=_('lesson start'))
    lesson_end = models.TimeField(default='16:30', verbose_name=_('lesson end'))
    num_of_pupils = models.PositiveIntegerField(verbose_name=_('number of pupils'))

    def __str__(self):
        return str(self.name)
    
    def get_first_image(self):
        """Helper method to get the first image URL"""
        image = self.schoolclassimage_set.first()
        return image.image.url if image else None
    
    def get_formatted_date(self):
        """Method for formatting dates: MM DD"""
        if self.start_date:
            return self.start_date.strftime("%b %d")
        return ""
    
    def get_formatted_year(self):
        """Method for formatting the year: YYYY"""
        if self.start_date:
            return self.start_date.strftime("%Y")
        return ""

    class Meta:
        verbose_name = _('class')
        verbose_name_plural = _('classes')

class SchoolClassImage(BaseModel):
    image = models.ImageField(upload_to='media/class/images', verbose_name=_('image'))
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE, verbose_name=_('class'))

    def __str__(self):
        return str(self.image.name)

    class Meta:
        verbose_name = _('class image')
        verbose_name_plural = _('class images')

class GalleryCategory(BaseModel):
    name = models.CharField(max_length=50, verbose_name=_('name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Gallery category')
        verbose_name_plural = _('Gallery categories')

class Gallery(BaseModel):
    title = models.CharField(max_length=128, verbose_name=_('title'))
    image = models.ImageField(upload_to='media/gallery', verbose_name=_('image'))
    gallery_category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE, verbose_name=_('gallery category'))

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _('Gallery')
        verbose_name_plural = _('Galleries')