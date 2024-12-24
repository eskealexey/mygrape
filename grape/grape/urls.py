"""
URL configuration for grape project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app.views import index
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from grape import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', index, name='home'),
    path('sorts/', include('spravgrape.urls'), name='sorts'),
    path('users/', include('users.urls'), name='users'),
    path('preparats/', include('preparats.urls'), name='preparats'),
    path('sickpest/', include('sickpest.urls'), name='sickpest'),
    path('dung/', include('dung.urls'), name='dung'),
    path('jornal/', include('jornal.urls'), name='jornal'),
    path('record/', include('record.urls'), name='record'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
