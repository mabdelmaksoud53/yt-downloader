# Description: Download YouTube videos and playlists using yt-dlp.
# Usage: python main.py
# Credits: Mostafa S. Abd El-Maksoud (https://www.github.com/mabdelmakosud53)
# Created: 2025-03-01 - 20:00:00
# Modified: 2025-03-05 - 20:00:00

from downloader import download_video, download_playlist
from utils import create_download_folder

if __name__ == "__main__":
    create_download_folder()

    url = input("Enter YouTube Video or Playlist URL: ").strip()
    resolution = input("Enter preferred resolution (e.g., 1080, 720, 480, best): ").strip()

    if "playlist" in url.lower():
        download_playlist(url, resolution)
    else:
        download_video(url, resolution)
