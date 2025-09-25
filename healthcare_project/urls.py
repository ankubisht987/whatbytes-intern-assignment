from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include all URLs from the 'api' app under the 'api/' prefix
    path('api/', include('api.urls')),
]