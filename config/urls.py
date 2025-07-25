from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    path('admin/', admin.site.urls),
    # CKEditor uploader url
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('school.urls')),
    path('news/', include('news.urls')),



    prefix_default_language=False
)