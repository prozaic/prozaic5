from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'new_sites'

urlpatterns = [ 

    path('', views.index, name = 'index'),

    path('topics/', views.topics, name = 'topics'),
    
    path('topic_edit/<int:topic_id>/', views.topic_edit, name='topic_edit'),

    path('delete_topic/<int:topic_id>/', views.delete_topic, name = 'delete_topic'),
   
    path('delete_topichome/<int:topic_id>/', views.delete_topichome, name = 'delete_topichome'),   

    path('delete_book/<int:book_id>/', views.delete_book, name = 'delete_book'),

    path('new_topic/', views.new_topic, name='new_topic'),

    path('new_topichome/', views.new_topichome, name='new_topichome'),

    path('vupload/', views.vupload, name ='vupload'),

    path('upload/', views.upload, name = 'upload'),

    path('books/', views.book_list, name = 'book_list'),

    path('books/uploads', views.upload_book, name = 'upload_book'),

    path('books/uploads/more', views.morebooks, name = 'morebooks'),

    path('contacts/', views.contact, name = 'contact')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)