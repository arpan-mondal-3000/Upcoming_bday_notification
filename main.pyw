from datetime import datetime, timedelta
import sqlite3
from winotify import Notification, audio
import time

# get today's date from datetime
today = datetime.now()

# calculate tomorrow's date
next_date = today + timedelta(days=1)

# get formatted date in required format
formatted_date = next_date.strftime("%d-%m-%Y")

# connecting to the database using sqlite3
connection = sqlite3.connect("userdata.db")
cursor = connection.cursor()

# creating the query
query = f"SELECT name FROM userdata WHERE dob LIKE '{formatted_date[:-4]}%'"

# executing the query
cursor.execute(query)
rows = cursor.fetchall()

# closing the sqlite cursor and connection
cursor.close()
connection.close()

# print(rows)

# showing the windows notification
if len(rows) == 0:
    pass
else:
    for i in range(0, len(rows)):
        message = f"{rows[i][0].title()}: {formatted_date}"
        toast = Notification(app_id="Birthday Notification",
                             title="Birthday Alert",
                             msg=message,
                             duration="short",
                             icon=r"E:\Fun Projects\Upcoming_bday_notification\cake.png")

        toast.set_audio(audio.Default, loop=False)
        toast.show()
        if (i != len(rows) - 1):
            time.sleep(5)
