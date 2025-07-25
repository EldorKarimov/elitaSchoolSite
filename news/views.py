from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import News, NewsCategory, Tag

class NewsListView(View):
    def get(self, request):
        news = News.objects.filter(is_published = True).order_by('-created')
        context = {
            'news':news
        }
        return render(request, 'news/news-list.html', context)
    
class NewsDetailView(View):
    def get(self, request, news_slug):
        new = get_object_or_404(News, slug = news_slug)
        recent_news = News.objects.exclude(id = new.id).filter(is_published = True).order_by('-created')[:3]
        other_news = News.objects.exclude(id=new.id).filter(is_published=True, category_id=new.category_id)[:3]
        context = {
            'new':new,
            'recent_news': recent_news,
            'other_news': other_news,
            'categories': NewsCategory.objects.all(),
            'tags': Tag.objects.all(),
        }
        return render(request, 'news/news-detail.html', context)