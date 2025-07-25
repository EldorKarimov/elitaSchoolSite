from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from common.models import BaseModel

User = get_user_model()

class Science(BaseModel):
    name = models.CharField(max_length=50, verbose_name=_("Fan nomi"))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Fan')
        verbose_name_plural = _('Fanlar')
    
class Hobby(BaseModel):
    name = models.CharField(max_length=50, verbose_name=_("Qiziqish nomi"))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Qiziqish')
        verbose_name_plural = _('Qiziqishlar')

class Position(BaseModel):
    name = models.CharField(_("lavozim nomi"), max_length=100)
    priority = models.IntegerField(_("tartib raqami"), default=0)
    is_leadership = models.BooleanField(_("rahbariyat a'zosi"), default=False)
    
    class Meta:
        verbose_name = _("Lavozim")
        verbose_name_plural = _("Lavozimlar")
        ordering = ['priority']
    
    def __str__(self):
        return self.name
    
class Teacher(BaseModel):
    DEGREE_CHOICES = [
        ('BACHELOR', _("Bakalavr")),
        ('MASTER', _("Magistr")),
        ('PHD', _("PhD (Fan doktori)")),
        ('DSC', _("Fan doktori (DSc)")),  # Doctor of Sciences
        ('PROFESSOR', _("Professor")),
        ('ASSOCIATE_PROF', _("Dotsent")),
        ('RESEARCHER', _("Katta ilmiy xodim")),
    ]
    
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        verbose_name=_("Foydalanuvchi")
    )
    image = models.ImageField(
        upload_to='accounts/teacher/', 
        verbose_name=_("Rasm")
    )

    # 90x90 PNG small image
    image_small = ImageSpecField(
        source='image',
        processors=[ResizeToFill(90, 90)],
        format='PNG',
        options={'quality': 100}
    )

    # 102x102 PNG medium image
    image_medium = ImageSpecField(
        source='image',
        processors=[ResizeToFill(102, 102)],
        format='PNG',
        options={'quality': 100}
    )

    experience = models.CharField(
        max_length=255, 
        verbose_name=_("Tajriba")
    )
    phone = models.CharField(
        max_length=13, 
        verbose_name=_("Telefon raqami")
    )
    about = RichTextUploadingField(
        verbose_name=_("O'qituvchi haqida")
    )
    hobbies = models.ManyToManyField(
        Hobby, 
        verbose_name=_("Qiziqishlari")
    )
    sciences = models.ManyToManyField(
        Science, 
        verbose_name=_("Fanlar")
    )
    degree_type = models.CharField(
        max_length=15, 
        choices=DEGREE_CHOICES, 
        default="BACHELOR",
        verbose_name=_("Ilmiy daraja")
    )
    position = models.ForeignKey(
        Position,
        on_delete=models.SET_NULL, 
        null=True,
        verbose_name=_("Lavozim")
    )

    class Meta:
        verbose_name = _("O'qituvchi")
        verbose_name_plural = _("O'qituvchilar")

    def __str__(self):
        return str(self.user.get_full_name())
    

class Skill(BaseModel):
    name = models.CharField(max_length=50, verbose_name=_('Koʻnikma nomi'))
    percent = models.PositiveIntegerField(verbose_name=_('Foiz'))
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name=_('Oʻqituvchi'))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Koʻnikma')
        verbose_name_plural = _('Koʻnikmalar')

class TeacherSchedule(BaseModel):
    teacher = models.ForeignKey(Teacher, related_name='teacher', on_delete=models.CASCADE, verbose_name=_('Oʻqituvchi'))
    weekday = models.CharField(max_length=50, verbose_name=_('Hafta kuni'))
    time_from = models.TimeField(verbose_name=_('Boshlanish vaqti'))
    time_to = models.TimeField(verbose_name=_('Tugash vaqti'))

    def __str__(self):
        return str(self.teacher.user.get_full_name)
    
    class Meta:
        verbose_name = _('Oʻqituvchi dars jadvali')
        verbose_name_plural = _('Oʻqituvchilar dars jadvallari')
 

class SchoolClass(BaseModel):
    class TransportationChoices(models.TextChoices):
        AVAILABLE = 'AVAILABLE', _('Mavjud')
        UNAVAILABLE = 'UNAVAILABLE', _('Mavjud emas')
        
    name = models.CharField(max_length=50, verbose_name=_('Sinf nomi'))
    slug = models.SlugField(max_length=50, unique=True, verbose_name=_('Slug'))
    start_date = models.DateField(verbose_name=_('Boshlanish sanasi'))
    size = models.PositiveIntegerField(default=20, verbose_name=_('Sinf hajmi'))
    transportation = models.CharField(max_length=11, choices=TransportationChoices.choices, verbose_name=_('Transport xizmati'))
    food = models.CharField(max_length=50, verbose_name=_('Ovqatlanish'))
    description = RichTextUploadingField(verbose_name=_('Tavsif'))
    image_card = models.ImageField(upload_to='class/images/card', null=True, verbose_name=_("Sinf rasmi kard"))
    pupil_birth_year = models.PositiveIntegerField(
        default=2015,
        validators=[MinValueValidator(2000), MaxValueValidator(2025)],
        verbose_name=_("Yosh toifasi (tug'ilgan yil)")
    )
    head_teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        related_name='teacher_classes',
        verbose_name=_('Sinf rahbari'),
    )
    teachers = models.ManyToManyField(Teacher, verbose_name=_('Oʻqituvchilar'))
    lesson_start = models.TimeField(default='08:30', verbose_name=_('Dars boshlanishi'))
    lesson_end = models.TimeField(default='16:30', verbose_name=_('Dars tugashi'))
    num_of_pupils = models.PositiveIntegerField(verbose_name=_('Oʻquvchilar soni'))

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
        """Method for formatting dates: YY"""
        if self.start_date:
            return self.start_date.strftime("%Y")
        return ""
    
    @property
    def get_pupil_age(self):
        age = timezone.now().year - self.pupil_birth_year
        return f"{age}-{age + 1}"

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = _('Sinf')
        verbose_name_plural = _('Sinflar')

class SchoolClassImage(BaseModel):
    image = models.ImageField(upload_to='class/images', verbose_name=_('Rasm'))
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE, verbose_name=_('Sinf'))

    def __str__(self):
        return str(self.image.name)

    class Meta:
        verbose_name = _('Sinf rasmi')
        verbose_name_plural = _('Sinf rasmlari')

class GalleryCategory(BaseModel):
    name = models.CharField(max_length=50, verbose_name=_('Kategoriya nomi'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Galereya kategoriyasi')
        verbose_name_plural = _('Galereya kategoriyalari')

class Gallery(BaseModel):
    title = models.CharField(max_length=128, verbose_name=_('Sarlavha'))
    image = models.ImageField(upload_to='gallery/', verbose_name=_('Rasm'))
    gallery_category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE, verbose_name=_('Galereya kategoriyasi'))

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _('Galereya')
        verbose_name_plural = _('Galereyalar')