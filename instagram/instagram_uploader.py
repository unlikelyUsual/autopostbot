from instagrapi import Client
import logging, os, time, random
from dotenv import load_dotenv

cl = Client()
cl.login(os.environ.get("INSTA_USER_USERNAME"),os.environ.get("INSTA_USER_PASSWORD"))

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def upload_video_to_instagram(file_path, caption):
    max_attempts = 3
    for attempt in range(max_attempts):
        try:
            cl.photo_upload(path=file_path, caption=caption)
            logger.info(f"Posted image: {file_path}")
            return
        except Exception as e:
            logger.error(f"Error uploading image (attempt {attempt + 1}): {str(e)}")
            if "Please wait a few minutes before you try again" in str(e):
                exponential_backoff(attempt)
            elif attempt == max_attempts - 1:
                raise

def exponential_backoff(attempt, max_delay=3600):
    delay = min(30 * (2 ** attempt), max_delay)
    time.sleep(delay + random.uniform(0, 10))