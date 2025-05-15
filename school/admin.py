from django.contrib import admin
from .models import *
from django.utils.translation import gettext_lazy as _

@admin.register(Science)
class ScienceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    list_per_page = 20

@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    list_per_page = 20

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 0
    fields = ('name', 'percent')

class ScheduleInline(admin.TabularInline):
    model = TeacherSchedule
    extra = 0
    fields = ('weekday', 'time_from', 'time_to')

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name', 'priority', 'is_leadership', 'created', 'updated')
    search_fields = ('name', )
    list_filter = ('priority', 'is_leadership')
    ordering = ('priority', )
    readonly_fields = ('created', 'updated')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'experience', 'phone')
    search_fields = ('user__first_name', 'user__last_name', 'phone')
    list_filter = ('sciences', 'hobbies')
    ordering = ('user__last_name', 'user__first_name')
    filter_horizontal = ('sciences', 'hobbies')
    inlines = [SkillInline, ScheduleInline]
    readonly_fields = ('image_preview',)
    fieldsets = (
        (_('Personal Information'), {
            'fields': ('user', 'image', 'image_preview', 'phone')
        }),
        (_('Professional Information'), {
            'fields': ('position', 'experience', 'about')
        }),
        (_('Interests'), {
            'fields': ('sciences', 'hobbies')
        }),
    )

    def get_full_name(self, obj):
        return obj.user.get_full_name()
    get_full_name.short_description = _('Full Name')
    get_full_name.admin_order_field = 'user__last_name'

    def image_preview(self, obj):
        from django.utils.html import format_html
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return "-"
    image_preview.short_description = _('Image Preview')


class SchoolClassImageInline(admin.TabularInline):
    model = SchoolClassImage
    extra = 1
    fields = ('image', )

@admin.register(SchoolClass)
class SchoolClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'size', 'transportation', 'head_teacher', 'num_of_pupils')
    list_filter = ('start_date', 'transportation', 'head_teacher')
    search_fields = ('name', 'description')
    filter_horizontal = ('teachers',)
    inlines = (SchoolClassImageInline, )
    fieldsets = (
        (_('Basic Information'), {
            'fields': ('name', 'slug', 'description')
        }),
        (_('Class Details'), {
            'fields': ('start_date', 'size', 'transportation', 'food')
        }),
        (_('Schedule'), {
            'fields': ('lesson_start', 'lesson_end')
        }),
        (_('Teachers'), {
            'fields': ('head_teacher', 'teachers')
        }),
        (_('Students'), {
            'fields': ('num_of_pupils',)
        }),
    )
    prepopulated_fields = {'slug': ('name',)}


@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'gallery_category', 'image')
    list_filter = ('gallery_category',)
    search_fields = ('title', 'gallery_category__name')
    fieldsets = (
        (None, {
            'fields': ('title', 'gallery_category', 'image')
        }),
    )