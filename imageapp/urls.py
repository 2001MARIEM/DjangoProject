from django.urls import path
from . import views

urlpatterns = [
    #path('upload/', views.upload_image, name='upload_image'),  
    #path('dashboard/', views.dashboard, name='dashboard'),
    #path('', views.home, name='home'),
    path('', views.dashboard, name='dashboard'),path('image/<str:file_id>/', views.serve_image, name='serve_image'),
]
