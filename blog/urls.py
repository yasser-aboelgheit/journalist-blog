from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('home.urls')),
    path('articles/', include('articles.urls')),
    path('coverages/', include('coverages.urls')),
    path('investigations/', include('investigations.urls')),
    path('documentaries/', include('documentaries.urls')),
    path('podcast/', include('podcast.urls')),
    path('blogs/', include('blogs.urls')),
    path('about-me/', include('about_me.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)