from django.contrib import admin
from django.urls import path, include

from indexer import views

app_name = 'indexer'

urlpatterns = [
    path('', views.Index.as_view()),

]
