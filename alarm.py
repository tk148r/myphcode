
import time
from datetime import datetime
import winsound

# Take alarm time from user
alarm_time = input("Enter alarm time (HH:MM:SS): ")

print("Alarm set for", alarm_time)

while True:
    current_time = datetime.now().strftime("%H:%M:%S")

    if current_time == alarm_time:
        print("⏰ WAKE UP! ALARM IS RINGING!")

        # Play alarm sound
        for i in range(10):
            winsound.Beep(1000, 1000)
            time.sleep(0.5)

        break

    time.sleep(1)
