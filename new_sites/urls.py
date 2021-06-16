from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'new_sites'

urlpatterns = [ 

    path('', views.index, name = 'index'),

    path('videos/', views.videos, name = 'videos'),
    
    path('video_edit/<int:video_id>/', views.video_edit, name='video_edit'),

    path('post_edit/<int:topic_id>/', views.post_edit, name='post_edit'),

    path('delete_video/<int:topic_id>/', views.delete_video, name = 'delete_video'),

    path('delete_post/<int:topic_id>/', views.delete_post, name = 'delete_post'),
   
    path('delete_topichome/<int:topic_id>/', views.delete_topichome, name = 'delete_topichome'),   

    path('delete_book/<int:book_id>/', views.delete_book, name = 'delete_book'),

    path('new_topic/', views.new_topic, name='new_topic'),

    path('new_post/', views.new_post, name='new_post'),

    path('new_topichome/', views.new_topichome, name='new_topichome'),

    path('vupload/', views.vupload, name ='vupload'),

    path('upload/', views.upload, name = 'upload'),

    path('books/', views.book_list, name = 'book_list'),

    path('posts/', views.post_list, name = 'post_list'),

    path('books/uploads', views.upload_book, name = 'upload_book'),

    path('books/uploads/more', views.morebooks, name = 'morebooks'),

    path('contacts/', views.contact, name = 'contact')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
