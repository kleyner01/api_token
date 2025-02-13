# app/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('pedidos.urls')),
    path('api/v1/', include('custom_token.urls')),
    path('api/v1/', include('custom_email.urls')),
]
