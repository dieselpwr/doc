from django.urls import path, include
from doc import views

urlpatterns = [
    path('', views.home, name='doc_home'),
]
