from modeltranslation.translator import TranslationOptions, register

from news.models import NewsCategory, Tag, News
from school.models import Science, Hobby, Teacher, Skill, TeacherSchedule, SchoolClass, Gallery, GalleryCategory


# for news app
@register(NewsCategory)
class NewsCategoryTranslationOptions(TranslationOptions):
    fields = ('name', )

@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ('name', )

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


# for school app
@register(Science)
class ScienceTranslationOptions(TranslationOptions):
    fields = ('name', )

@register(Hobby)
class HobbyTranslationOptions(TranslationOptions):
    fields = ('name', )

@register(Teacher)
class TeacherTranslationOptions(TranslationOptions):
    fields = ('experience', 'about', )

@register(Skill)
class SkillTranslationOptions(TranslationOptions):
    fields = ('name', )

@register(TeacherSchedule)
class TeacherScheduleTranslationOptions(TranslationOptions):
    fields = ('weekday', )

@register(SchoolClass)
class SchoolClassTranslationOptions(TranslationOptions):
    fields = ('name', 'food', 'description')

@register(GalleryCategory)
class GalleryCategoryTranslationOptions(TranslationOptions):
    fields = ('name', )

@register(Gallery)
class GalleryTranslationOptions(TranslationOptions):
    fields = ('title', )