import requests
import os
from urllib.parse import urlparse
from pathlib import Path

def download_video(url, filename_prefix = ''):
    image_folder = 'images'
    os.makedirs(image_folder, exist_ok=True)
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise exception for bad status

        # Determine filename
        if filename_prefix:
            filename_prefix = filename_prefix.replace(" ", "_") + "_"  # Replace spaces
        parsed_url = urlparse(url)
        path = parsed_url.path
        # Get the name after the last '/'
        filename = os.path.basename(path)
        if not filename:
            filename = "downloaded_file"
        if "." not in filename:
            content_type = response.headers.get('content-type')
            if content_type:
                if 'image' in content_type:
                    file_extension = content_type.split('/')[1].split(';')[0]
                    filename = f"{filename}.{file_extension}"
                elif 'video' in content_type:
                    file_extension = content_type.split('/')[1].split(';')[0]
                    filename = f"{filename}.{file_extension}"
                else:
                    filename = f"{filename}.dat" #just download with .dat
            else:
                filename = f"{filename}.dat"

        filename = filename_prefix + filename
        file_path = Path(image_folder) / filename

        with open(file_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):  # 8KB chunks
                file.write(chunk)
        print(f"Downloaded: {file_path}")
        return file_path  # Return the Path object
    except requests.exceptions.RequestException as e:
        print(f"Error downloading from {url}: {e}")
        return None
    except Exception as e:
        print(f"An error occurred while processing {url}: {e}")
        return None