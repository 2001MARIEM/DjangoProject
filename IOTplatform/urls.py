from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from imageapp.views import home
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('imageapp.urls')),
    path('', home, name='home'), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


