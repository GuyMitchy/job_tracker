from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.core.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('applications/', include('apps.applications.urls')),
    path('networking/', include('apps.networking.urls')),
    path('targets/', include('apps.targets.urls')),
    path('analytics/', include('apps.analytics.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 