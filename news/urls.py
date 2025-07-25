from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    path('list/', views.NewsListView.as_view(), name='news_list'),
    path('<slug:news_slug>/', views.NewsDetailView.as_view(), name='news_detail')
]