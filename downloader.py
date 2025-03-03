import os
import yt_dlp

def download_video(url, resolution="best"):
    """Download a single YouTube video at the specified resolution."""
    os.makedirs("Downloads", exist_ok=True)
    
    ydl_opts = {
        'format': f'bestvideo[height<={resolution}]+bestaudio/best',
        'outtmpl': 'Downloads/%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_playlist(url, resolution="best"):
    """Download all videos from a YouTube playlist."""
    os.makedirs("Downloads", exist_ok=True)
    
    ydl_opts = {
        'format': f'bestvideo[height<={resolution}]+bestaudio/best',
        'outtmpl': 'Downloads/%(playlist)s/%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
