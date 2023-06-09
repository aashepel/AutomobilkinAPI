"""
URL configuration for AutomobilkinAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from AutomobilkinAPI import settings
from AutomobilkinAPIApp.views import AutoConcernViewSet, ModelCarViewSet, ModelCarGenerationViewSet, CarViewSet

api_router = routers.DefaultRouter()
api_router.register(r'concerns', AutoConcernViewSet)
api_router.register(r'models', ModelCarViewSet)
api_router.register(r'models_gen', ModelCarGenerationViewSet)
api_router.register(r'cars', CarViewSet)

urlpatterns = [
    path('api/', include(api_router.urls)),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
