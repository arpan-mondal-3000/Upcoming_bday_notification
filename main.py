import datetime
import sqlite3
from winotify import Notification, audio
import time


def upcoming_bdays():
    current_datetime = datetime.datetime.now()
    current_month = current_datetime.month
    current_month = 11
    current_date = current_datetime.date()

    connection = sqlite3.connect("userdata.db")
    cursor = connection.cursor()

    if len(str(current_month)) == 1:
        query = f"SELECT id,name,dob FROM userdata WHERE dob LIKE '%-0{current_month}-%'"
    else:
        query = f"SELECT id,name,dob FROM userdata WHERE dob LIKE '%-{current_month}-%'"

    cursor.execute(query)
    rows = cursor.fetchall()

    upcoming_bdays = []
    for i in range(0, len(rows)):
        name = rows[i][1]
        dob = rows[i][2]

        if int(dob[:2]) >= int(str(current_date)[-2:]):
            upcoming_bdays.append(f"{name.title()} - {dob[:2]}/{dob[3:5]}")

    cursor.close()
    connection.close()
    return upcoming_bdays


print(upcoming_bdays(), len(upcoming_bdays()))

for i in range(0, len(upcoming_bdays())):
    message = f"{upcoming_bdays()[i]}"
    toast = Notification(app_id="Birthday Notification",
                         title="Birthday Alert",
                         msg=message,
                         duration="short",
                         icon=r"E:\Fun Projects\Upcoming_bday_notification\cake.png")

    toast.set_audio(audio.Default, loop=False)
    toast.show()
    if (i != len(upcoming_bdays()) - 1):
        time.sleep(5)
