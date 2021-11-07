from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('vortex_core.urls')),
    path('', include('vortex_core.urls')),
]
