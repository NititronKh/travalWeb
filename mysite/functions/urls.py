from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('submit/', views.submit_content, name='submit_content'),
    path('content1/', views.content1, name='content1'),
    path('content2/', views.content2, name='content2'),
    path('content3/', views.content3, name='content3'),
    path('content4/', views.content4, name='content4'),
    path('content5/', views.content5, name='content5'),
    path('edit/<int:content_id>/', views.edit_content, name='edit_content'),
    path('delete/<int:content_id>/', views.delete_content, name='delete_content'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
    document_root=settings.MEDIA_ROOT)