from django.conf.urls import handler404, handler500
from django.contrib import admin
from django.urls import path , include 
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("cinolu_event_app.urls") ),
]

handler404 = 'cinolu_event_app.views.error_404'
handler500 = 'cinolu_event_app.views.error_500'


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
