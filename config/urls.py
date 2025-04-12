from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # CKEditor uploader url
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
