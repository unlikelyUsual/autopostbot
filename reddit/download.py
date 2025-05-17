# download_media.py
import yt_dlp
from pathlib import Path
import os

def download_video(video_url, title):

    videos_folder = "videos"
    os.makedirs(videos_folder, exist_ok=True)
    sanitized_title = "".join(c if c.isalnum() else "_" for c in title[:50])  # Sanitize title
    output_template = f"{videos_folder}/{sanitized_title}.%(ext)s"

    ydl_opts = {
        'outtmpl': output_template,
        'merge_output_format': 'mp4',
        'quiet': True,
        'noplaylist': True,
         'retries': 3,  # Retry failed downloads
        'nocheckcertificate': True, # Bypass SSL certificate verification
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # print(f"Downloading: {video_url}")
            # ydl.download([video_url])
            # print(f"Download completed: {title}.mp4")
            info_dict = ydl.extract_info(video_url, download=True)  # Download and get info
            if info_dict and 'filename' in info_dict:
                downloaded_file_path = Path(info_dict['filename'])
                print(f"Downloaded successfully to: {downloaded_file_path}")
                return downloaded_file_path
            else:
                print(f"Download failed: No filename returned by yt_dlp")
                return None
    except Exception as e:
        print(f"Failed to download video from {video_url}: {e}")
