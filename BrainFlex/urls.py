from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# Set the Django admin header
admin.site.site_header = 'BrainFlex'
from django.urls import path
from django.conf.urls import handler404
from quiz.views.custom_404 import custom_404_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quiz.urls', namespace='quiz')),  # Include app's URLs with namespace
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Define a custom handler404 view
handler404 = 'quiz.views.custom_404.custom_404_page'