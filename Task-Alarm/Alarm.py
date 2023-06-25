import datetime
import time

def set_alarm():
    alarm_time = input("Enter the alarm time (in HH:MM:SS format): ")
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print("Current Time:", current_time)
    print("Alarm Time:", alarm_time)

    while current_time != alarm_time:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        time.sleep(1)

    print("Wake up!")

set_alarm()
