from app.views import index
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.clickjacking import xframe_options_exempt
from filebrowser.sites import site

from grape import settings

urlpatterns = [
    path('admin/filebrowser/', site.urls),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    # path('admin/', admin.site.urls),
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
