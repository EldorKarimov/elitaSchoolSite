from django.shortcuts import render
from django.views import View

from common.models import Slider, About
from news.models import News, NewsCategory, Tag
from .models import SchoolClass

class HomePageView(View):
    def get(self, request):
        sliders = Slider.objects.filter(is_available = True)
        classes = SchoolClass.objects.all()[:5]
        context = {
            'sliders':sliders,
            'classes':classes
        }
        return render(request, 'school/index.html', context)