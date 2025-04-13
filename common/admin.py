from django.contrib import admin

# Register your models here.
from .models import Slider, About

admin.site.register([Slider, About])