from django.urls import path
from . import views

app_name = 'school'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('class-details/<slug:slug>', views.SchoolClassDetailView.as_view(), name='class-details'),
    path('teacher-info/<uuid:teacher_id>', views.TeacherDetailsView.as_view(), name='teacher_info'),
    path('gallery/', views.GalleryListView.as_view(), name='gallery_list'),
    path('gallery/<uuid:category_id>/', views.GalleryListView.as_view(), name='gallery_list_by_category'),
    path('class-list/', views.SchoolClassesList.as_view(), name='school_class_list'),
]