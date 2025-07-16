from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import JsonResponse
from uuid import UUID

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
        
        context = {
            'sliders': sliders,
            'classes': classes,
            'teachers': teachers,
            'director': director,
            'gallery_categories': gallery_categories,
            'galleries': galleries,
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
        other_classes = SchoolClass.objects.exclude(slug = slug)
        context = {
            'school_class':school_class,
            'other_classes':other_classes
        }
        return render(request, 'school/class-details.html', context)
    

class GalleryAjaxView(View):
    def get(self, request, *args, **kwargs):
        cat_id = request.GET.get('category_id')
        print('AJAX category_id:', cat_id)

        if cat_id == 'all':
            photos = Gallery.objects.all()
        else:
            try:
                cat_uuid = UUID(cat_id)  # ← bu yerda UUID obyektga aylantiramiz
                photos = Gallery.objects.filter(gallery_category__id=cat_uuid)
            except ValueError:
                return JsonResponse({'images': []})

        data = [
            {
                'title': p.title,
                'image_url': p.image.url,
                'category_class': p.gallery_category.name.lower().replace(' ', '-')
            } for p in photos
        ]
        return JsonResponse({'images': data})
