from django.shortcuts import render, get_object_or_404
from django.views import View

from common.models import Slider, About
from news.models import News, NewsCategory, Tag
from .models import SchoolClass, Teacher

class HomePageView(View):
    def get(self, request):
        sliders = Slider.objects.filter(is_available = True)
        classes = SchoolClass.objects.all()[:5]
        teachers = Teacher.objects.all().order_by('-degree_type')
        context = {
            'sliders':sliders,
            'classes':classes,
            'teachers':teachers,
            'featured_teacher':teachers.first()
        }
        return render(request, 'school/index.html', context)
    
class SchoolClassListView(View):
    def get(self, request):
        school_classes = SchoolClass.objects.all()
        context = {
            'classes':school_classes
        }
        return render(request, 'school/classes.html', context)

class SchoolClassDetailView(View):
    def get(self, request, slug):
        school_class = get_object_or_404(SchoolClass, slug = slug)
        context = {
            'school_class':school_class
        }
        return render(request, 'school/class-details.html', context)