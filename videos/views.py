from django.shortcuts import render, redirect
from .forms import VideoUploadForm
from .models import Video
from django.db.models import Q

# Create your views here.
def upload_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()
            video.extract_subtitles()  # Extract subtitles after saving
            return redirect('video_list')
    else:
        form = VideoUploadForm()
    return render(request, 'videos/upload.html', {'form': form})


def search_videos(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        results = Video.objects.filter(Q(subtitle_content__icontains=query))
    return render(request, 'videos/search.html', {'query': query, 'results': results})


def video_list(request):
    videos = Video.objects.all()
    return render(request, 'videos/list.html', {'videos': videos})

def view_video(request, video_id):
    video = Video.objects.get(id=video_id)
    return render(request, 'videos/detail.html', {'video': video})


