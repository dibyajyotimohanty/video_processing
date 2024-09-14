from django.urls import path
from .views import upload_video, video_list, search_videos, view_video



urlpatterns = [
    path('upload/', upload_video, name='upload_video'),
    path('videos/', video_list, name='video_list'),
    path('search/', search_videos, name='search_videos'),
    path('videos/<int:video_id>/', view_video, name='view_video'),
]


