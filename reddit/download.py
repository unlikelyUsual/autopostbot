import yt_dlp
from pathlib import Path
import os

def download_video(video_url, title):
    videos_folder = "videos"
    os.makedirs(videos_folder, exist_ok=True)

    # Sanitize title and prepare output path
    sanitized_title = "".join(c if c.isalnum() else "_" for c in title[:50])
    output_template = f"{videos_folder}/{sanitized_title}.%(ext)s"

    ydl_opts = {
        'outtmpl': output_template,
        'merge_output_format': 'mp4',
        'quiet': True,
        'noplaylist': True,
        'retries': 3,
        'nocheckcertificate': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=True)

            if info_dict:
                # Get the correct extension (usually mp4)
                ext = info_dict.get('ext', 'mp4')
                final_filename = f"{sanitized_title}.{ext}"
                final_path = Path(videos_folder) / final_filename

                if final_path.exists():
                    print(f"✅ Downloaded successfully to: {final_path}")
                    return final_path
                else:
                    print(f"⚠️ Expected file not found: {final_path}")
                    return None
            else:
                print("❌ Download failed: yt_dlp returned no info")
                return None

    except Exception as e:
        print(f"❌ Failed to download video from {video_url}: {e}")
        return None
