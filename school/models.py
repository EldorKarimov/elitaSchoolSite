from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

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
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('user'))
    image = models.ImageField(upload_to='media/accounts/teacher/', verbose_name=_('image'))
    experience = models.CharField(max_length=255, verbose_name=_('experience'))
    phone = models.CharField(max_length=13, verbose_name=_('phone'))
    about = models.TextField(verbose_name=_('about teacher'))
    hobbies = models.ManyToManyField(Hobby, verbose_name=_('hobbies'))
    sciences = models.ManyToManyField(Science, verbose_name=_('sciences'))

    def __str__(self):
        return str(self.user.get_full_name)

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
 
 