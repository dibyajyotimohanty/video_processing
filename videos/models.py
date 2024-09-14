from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/')
    subtitle_file = models.FileField(upload_to='subtitles/', null=True, blank=True)
    subtitle_content = models.TextField(null=True, blank=True)  # Store subtitles as text
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def extract_subtitles(self):
        import os
        from subprocess import run

        # Build paths
        video_path = self.video_file.path
        subtitle_output_path = os.path.join(os.path.dirname(video_path), f"{self.title}.srt")

        import string
        video_path = video_path.replace("\\\\", "\\")
        subtitle_output_path = subtitle_output_path.replace("\\\\", "\\")
        print('--subtitle_output_path--',subtitle_output_path)

        # Run ccextractor to extract subtitles
        # run(['ccextractor', video_path, '-o', subtitle_output_path], check=True)
        # run(['ccextractorwinfull', video_path, '-o', subtitle_output_path], check=True)
        run(['mkvextract', 'tracks', video_path, f'2:{subtitle_output_path}'], check=True)

        # Save the subtitle file path to the model
        self.subtitle_file.name = f"subtitles/{self.title}.srt"

        # Read the subtitle file and store its content
        with open(subtitle_output_path, 'r', encoding='utf-8') as subtitle_file:
            self.subtitle_content = subtitle_file.read()
        
        self.save()
