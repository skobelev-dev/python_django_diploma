"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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

from my_auth.views import ProfileViewSet
from catalogapp.views import ProductViewSet
from payment.views import PaymentGenericViewSet
from .settings import DEBUG, MEDIA_URL, MEDIA_ROOT
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from catalogapp.views import TagViewSet

routers = DefaultRouter()

routers.register("products", ProductViewSet)
routers.register("tags", TagViewSet)
routers.register("profile", ProfileViewSet)
routers.register("payment", PaymentGenericViewSet)

urlpatterns = [
    path("api/", include(routers.urls)),
    path("", include("frontend.urls")),
    path("admin/", admin.site.urls),
    path("shop/", include("catalogapp.urls")),
]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
