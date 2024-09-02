from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),  #as_view() transforme la classe ImageUploadView en view
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.home, name='home'),
    path('image/<str:file_id>/', views.serve_image, name='serve_image'),
]
