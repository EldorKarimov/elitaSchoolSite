from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Contact
from django.utils.translation import gettext_lazy as _

# Custom User Admin
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'patronymic', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'patronymic')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    ordering = ('-date_joined',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'patronymic', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'patronymic', 'email'),
        }),
    )



# @admin.register(Skill)
# class SkillAdmin(admin.ModelAdmin):
#     list_display = ('name', 'percent', 'teacher')
#     search_fields = ('name', 'teacher__user__first_name', 'teacher__user__last_name')
#     list_filter = ('teacher',)
#     ordering = ('teacher__user__last_name', 'name')
#     list_per_page = 20

# @admin.register(TeacherSchedule)
# class TeacherScheduleAdmin(admin.ModelAdmin):
#     list_display = ('teacher', 'weekday', 'time_from', 'time_to')
#     search_fields = ('teacher__user__first_name', 'teacher__user__last_name', 'weekday')
#     list_filter = ('weekday', 'teacher')
#     ordering = ('teacher__user__last_name', 'weekday', 'time_from')
#     list_per_page = 20

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'subject', 'phone_or_email', 'created')
    search_fields = ('full_name', 'subject', 'phone_or_email', 'message')
    list_filter = ('created',)
    ordering = ('-created',)
    readonly_fields = ('created', 'updated')
    list_per_page = 20