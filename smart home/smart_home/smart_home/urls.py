"""smart_home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from measurement.views import SensorViewSet, MeasurementViewSet


router = routers.DefaultRouter()
router.register(r'sensors', SensorViewSet)
router.register(r'measurements', MeasurementViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/project', ProjectViewSet.as_view({'get': 'list'})),
    path('api/measurement', MeasurementViewSet.as_view({'get': 'list'})),
]