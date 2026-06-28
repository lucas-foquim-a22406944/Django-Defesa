from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('biblioteca/', include('biblioteca.urls')),
    path('escola/', include('escola.urls')),
    path('loja/', include('loja.urls')),
]
