from .views import BaseAPI,FileView
from django.urls import path

urlpatterns = [path('api/v0/testing',BaseAPI.as_view(), name='BaseAPI'),
               path('upload', FileView.as_view(), name='uploadfiles')]