import os

def create_download_folder():
    """Ensure the Downloads directory exists."""
    os.makedirs("Downloads", exist_ok=True)
