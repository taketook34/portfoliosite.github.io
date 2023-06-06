from django.urls import path, include
from .views import *

urlpatterns = [
    path('home/', home_page, name='home'),
    path('projects/', ListProjects.as_view(), name='projects'),
    path('projects/<int:post_id>/', show_post, name='post'),
    path('questions/', questions, name='questions')
]