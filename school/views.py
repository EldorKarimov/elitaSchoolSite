from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import JsonResponse
from uuid import UUID
from django.core.paginator import Paginator
from django.db.models import Q

from common.models import Slider, About
from news.models import News, NewsCategory, Tag
from .models import SchoolClass, Teacher, Gallery, GalleryCategory

class HomePageView(View):
    def get(self, request):
        sliders = Slider.objects.filter(is_available=True)
        classes = SchoolClass.objects.all()[:5]
        teachers = Teacher.objects.filter(position__priority__gte=2).order_by('-degree_type')
        director = Teacher.objects.filter(position__priority=1).first()
        gallery_categories = GalleryCategory.objects.all()
        galleries = Gallery.objects.all()[:8]

        news = News.objects.filter(is_published = True).order_by('-created')[:5]
        
        context = {
            'sliders': sliders,
            'classes': classes,
            'teachers': teachers,
            'director': director,
            'gallery_categories': gallery_categories,
            'galleries': galleries,
            'news':news
        }
        return render(request, 'school/index.html', context)
    
class SchoolClassListView(View):
    def get(self, request):
        school_classes = SchoolClass.objects.all()
        paginator = Paginator(school_classes, 1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'classes':page_obj
        }
        return render(request, 'school/class-list.html', context)

class SchoolClassDetailView(View):
    def get(self, request, slug):
        school_class = get_object_or_404(SchoolClass, slug = slug)
        other_classes = SchoolClass.objects.exclude(slug = slug)
        context = {
            'school_class':school_class,
            'other_classes':other_classes
        }
        return render(request, 'school/class-details.html', context)


class TeacherListView(View):
    def get(self, request):
        search = request.GET.get('search')
        page_num = request.GET.get('page')

        teachers = Teacher.objects.all().order_by('position__priority')
        if search:
            teachers = teachers.filter(Q(user__first_name = search)| Q(user__last_name = search))
        else:
            search = ''

        paginator = Paginator(teachers, 9)
        page_obj = paginator.get_page(page_num)
        context = {
            'teachers':page_obj,
            'search':search
        }
        return render(request, 'school/teachers.html', context)

        

class TeacherDetailsView(View):
    def get(self, request, teacher_id):
        teacher = get_object_or_404(Teacher, id=teacher_id)
        my_classes = SchoolClass.objects.filter(teachers__in=[teacher])
        context = {
            'teacher': teacher,
            'my_classes':my_classes
        }
        return render(request, 'school/teacher-info.html', context)

class GalleryListView(View):
    def get(self, request, category_id = None):
        galleries = Gallery.objects.all()
        if category_id:
            gallery_category = get_object_or_404(GalleryCategory, id=category_id)
            galleries = galleries.filter(gallery_category=gallery_category)

        gallery_categories = GalleryCategory.objects.all()
        paginator = Paginator(galleries, 15)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'galleries': page_obj,
            'gallery_categories': gallery_categories
        }
        return render(request, 'school/gallery.html', context)
    
class SchoolClassesList(View):
    def get(self, request):
        school_classes = SchoolClass.objects.all()
        paginator = Paginator(school_classes, 9)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'school_classes':page_obj
        }
        return render(request, 'school/class-list.html', context)