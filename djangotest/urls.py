"""djangotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers

from example.views import SchoolViewSet
from example.urls import router as example_router

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'schools', SchoolViewSet)  # this created http request routes
# also r'schools' will be the endpoint

router.registry.extend(example_router.registry)

urlpatterns = [
    path('api/', include(router.urls)),
]
