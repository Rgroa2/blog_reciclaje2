from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.urls.conf import include
from apps.ablog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('blog/', include('apps.ablog.urls'),),
    path('login/', include('apps.blog_auth.urls'),),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT, show_indexes=True)
