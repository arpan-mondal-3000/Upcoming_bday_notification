import datetime
import sqlite3
from winotify import Notification, audio
import time


def upcoming_bdays():
    current_datetime = datetime.datetime.now()
    current_month = current_datetime.month
    current_date = current_datetime.date()
    current_year = current_datetime.year
    connection = sqlite3.connect("userdata.db")
    cursor = connection.cursor()

    if int(current_month) == 2:
        if current_year % 4 == 0:
            last_date = 29
        else:
            last_date = 28
    elif int(current_month) % 2 != 0 or int(current_month) == 8:
        last_date = 31
    else:
        last_date = 30

    if len(str(current_month)) == 1:
        current_month = "0" + str(current_month)

    if current_date != last_date:
        query = f"SELECT id,name,dob FROM userdata WHERE dob LIKE '%-{current_month}-%'"
    else:
        if current_month != 12:
            current_month = int(current_month) + 1
            if len(str(current_month)) == 1:
                current_month = "0" + str(current_month)
            query = f"SELECT id,name,dob FROM userdata WHERE dob LIKE '01-{current_month}-%'"
        else:
            query = f"SELECT id,name,dob FROM userdata WHERE dob LIKE '01-01-%'"

    cursor.execute(query)
    rows = cursor.fetchall()

    upcoming_bdays = []
    for i in range(0, len(rows)):
        name = rows[i][1]
        dob = rows[i][2]

        if current_date != last_date:
            if int(dob[:2]) == int(str(current_date)[-2:]) + 1:
                upcoming_bdays.append(f"{name.title()} - {dob[:2]}/{dob[3:5]}")
        else:
            upcoming_bdays.append(f"{name.title()} - {dob[:2]}/{dob[3:5]}")
    cursor.close()
    connection.close()
    return upcoming_bdays


print(upcoming_bdays())

if len(upcoming_bdays()) == 0:
    pass
else:
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
