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
            'fields': ('experience', 'about')
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