from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_audio, name='upload'),
    path('form/', views.data_extraction_from_user, name='features')
]
