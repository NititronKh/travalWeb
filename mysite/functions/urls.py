from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('submit/', views.submit_content, name='submit_content'),
    path('show_content/', views.show_content, name='show_content'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
    document_root=settings.MEDIA_ROOT)