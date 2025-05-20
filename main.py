from pathlib import Path
# import schedule
# import time
# import pytz
from reddit.get_post import get_and_download_videos
from instagram.instagram_uploader import upload_video_to_instagram

def daily_task():
    print('Job Start 🏁')
    res = get_and_download_videos()
    print(f'{res} : {res["saved_path"], res["tag"]}')
    saved_path = res['saved_path']
    if saved_path:
        upload_video_to_instagram(Path(saved_path), res['tag'])
        saved_path.unlink()
        print('Job Finished ✅')
    else:
        print(f"Skipped ⚠️: {saved_path}")

# Schedules the daily_task function to run every day at 10:00 AM IST.
# def schedule_daily_task():
#     ist_timezone = pytz.timezone('Asia/Kolkata')

#     schedule.every().day.at("01:00", ist_timezone).do(daily_task)  

#     # Keep the script running to execute the scheduled tasks and Check for pending tasks every minute.
#     while True:
#         schedule.run_pending()
#         time.sleep(60)

# if __name__ == "__main__":
#     schedule_daily_task()

daily_task();