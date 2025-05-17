import schedule
import time
from datetime import datetime
import pytz

def daily_task():
    print(f"Running daily task at {datetime.now(pytz.timezone('Asia/Kolkata'))}") # using pytz

# Schedules the daily_task function to run every day at 10:00 AM IST.
def schedule_daily_task():
    ist_timezone = pytz.timezone('Asia/Kolkata')

    schedule.every().day.at("10:00", ist_timezone).do(daily_task)  

    # Keep the script running to execute the scheduled tasks and Check for pending tasks every minute.
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    schedule_daily_task()  # Start the scheduling process.
