from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quiz.urls', namespace='quiz')),  # Include app's URLs with namespace
]
