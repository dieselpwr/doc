from django.urls import path, include
from doc import views

urlpatterns = [
    path('', views.detect, name='doc_detect'),
    path('home', views.home, name='doc_home'),
]
